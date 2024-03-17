# -*- coding: utf-8 -*-
import os
import pathlib
import queue
from typing import Any, List, Optional, Dict, Tuple
from requests import HTTPError  # type: ignore[import]

import pytest
from pytest import PytestConfigWarning
from zephyr import API_V2, ZephyrScale  # type: ignore[import]

from ._jira_integration import Jira
from ._zephyr_interface import (
    Folder,
    ZephyrTestCase,
    TEST_STEPS_OVERWRITE,
    TEST_CASE_FOLDER_TYPE,
)


_default_report_mapping = {
    "passed": "Pass",
    "failed": "Fail",
    "skipped": "Not Executed",
    "xfailed": "Blocked",
    "xpassed": "Fail",
}

report_mapping = _default_report_mapping


def _fmt_zephyr_error(msg: str):
    return RuntimeError(f"zephyr: {msg}")


def register_report_mapping(mapping: Dict[str, str]):
    def _validate_mapping(mapping: Dict[str, str]):
        assert "passed" in mapping, "passed not found in mapping"
        assert "failed" in mapping, "failed not found in mapping"
        assert "xfailed" in mapping, "xfailed not found in mapping"
        assert "xpassed" in mapping, "xpassed not found in mapping"
        assert "skipped" in mapping, "skipped not found in mapping"

    _validate_mapping(mapping)
    global report_mapping
    report_mapping = mapping


def _result_mapping(result: str) -> str:
    return report_mapping[result]


class ZephyrManager:

    @classmethod
    def _load_config_params(cls, config: pytest.Config) -> Optional["ZephyrManager"]:
        kwargs = {}
        mandatory_params = [
            "zephyr_auth_token",
            "zephyr_project_key",
            "zephyr_jira_base_url",
            "zephyr_jira_email",
            "zephyr_jira_token",
        ]
        mandatory_absent = []
        for param in mandatory_params:
            attr = param.replace("zephyr_", "")  # strip the zephyr_ prefix
            if param in os.environ.keys():  # env var has priority
                value = os.environ[param]
            else:
                value = config.getini(param)
            if not value:
                mandatory_absent.append(param)
            else:
                kwargs[attr] = value
        if mandatory_absent:
            raise _fmt_zephyr_error(
                f"The following mandatory params not found in pytest ini file or sys env vars:\n"
                f"{', '.join(mandatory_absent)}\n"
                f"See README for list of parameters and their use."
            )
        # Check connection
        strict = config.getini("zephyr_strict") or False
        healthy = True
        error_string = ""
        zephyr_manager = None
        try:
            zephyr_manager = cls(**kwargs)
        except HTTPError as reason:
            healthy = False
            error_string = f"Could not connect to Zephyr. Reason: {repr(reason)}"
        if not healthy:
            if strict:
                raise _fmt_zephyr_error(error_string)
            else:
                config.issue_config_time_warning(
                    PytestConfigWarning(error_string), stacklevel=2
                )
        return zephyr_manager

    def __init__(
        self,
        auth_token: str,
        project_key: str,
        jira_base_url: str,
        jira_email: str,
        jira_token: str,
    ):
        self.zephyr_instance: ZephyrScale = ZephyrScale(
            token=auth_token, api_version=API_V2
        )
        self.project_key = project_key
        self.project_id = int(
            self.zephyr_instance.api.projects.get_project(self.project_key)["id"]
        )
        self.testcases: List[ZephyrTestCase] = self._get_all_testscases()
        zephyr_folders = self.zephyr_instance.api.folders.get_folders()
        folders_queue: queue.Queue[dict] = queue.Queue()
        for folder in zephyr_folders:
            folders_queue.put(folder)
        self.root_folder = self._populate_root_folder(folders_queue)
        self.jira_instance = Jira(jira_base_url, jira_email, jira_token)
        self.testcycle_key = None
        self.executor_id: "str | None" = None
        self.priority_mapping, self.default_priority = self._get_priority_mapping()
        self.status_mapping, self.default_status = self._get_status_mapping()

    def _get_priority_mapping(self) -> Tuple[Dict[str, int], str]:
        priorities = self.zephyr_instance.api.priorities.get_priorities(
            projectKey=self.project_key
        )
        ret = {}
        default_priority = ""
        for priority in priorities:
            ret[priority["name"]] = priority["id"]
            if priority["default"]:
                default_priority = priority["name"]
        return ret, default_priority

    def _get_status_mapping(self) -> Tuple[Dict[str, int], str]:
        statuses = self.zephyr_instance.api.statuses.get_statuses(
            projectKey=self.project_key, statusType="TEST_CASE"
        )
        ret = {}
        default_status = ""
        for status in statuses:
            ret[status["name"]] = status["id"]
            if status["default"]:
                default_status = status["name"]
        return ret, default_status

    def _get_all_testscases(self) -> List[ZephyrTestCase]:
        ret: List[ZephyrTestCase] = []
        zephyr_testcases = self.zephyr_instance.api.test_cases.get_test_cases(
            projectKey=self.project_key
        )
        for testcase_dict in zephyr_testcases:
            folder_id = None
            ownerId = None
            if testcase_dict["folder"]:
                folder_id = testcase_dict["folder"]["id"]
            if testcase_dict["owner"]:
                ownerId = testcase_dict["owner"]["accountId"]
            testcase = ZephyrTestCase(
                project_id=testcase_dict["project"]["id"],
                priorityId=testcase_dict["priority"]["id"],
                statusId=testcase_dict["status"]["id"],
                folder_id=folder_id,
                owner_id=ownerId,
                jira_issues=[
                    issue["issueId"] for issue in testcase_dict["links"]["issues"]
                ],
                urls=[weblink["url"] for weblink in testcase_dict["links"]["webLinks"]],
                jira_issues_links={
                    issue["issueId"]: issue["id"]
                    for issue in testcase_dict["links"]["issues"]
                },
                urls_links={
                    weblink["url"]: weblink["id"]
                    for weblink in testcase_dict["links"]["webLinks"]
                },
                **testcase_dict,
            )
            ret.append(testcase)
        return ret

    def _maybe_update_test_case(
        self, collected_test_case: ZephyrTestCase, original_test_case: ZephyrTestCase
    ) -> None:
        collected_dict = collected_test_case.to_dict()
        original_dict = original_test_case.to_dict()
        if collected_dict != original_dict:
            self.zephyr_instance.api.test_cases.update_test_case(
                test_case_key=collected_test_case.key,
                test_case_id=collected_test_case.id,
                **collected_dict,
            )

    def _create_test_case(
        self,
        name: str,
        folder: Folder,
        jira_issues: Optional[List[str]],
        urls: Optional[List[str]],
        test_steps: "List[Dict[str, str]] | str",
        extra_info: Dict[str, Any],
    ) -> str:
        if not jira_issues:
            jira_issues = []
        issue_ids: List[int] = []
        for jira_issue in jira_issues:
            if jira_issue.isnumeric():
                jira_issue = f"{self.project_key}-{jira_issue}"
            id_ = self.jira_instance.get_issue_id(jira_issue)
            issue_ids.append(id_)
        extra_info["jira_issues"] = issue_ids
        if not urls:
            urls = []
        extra_info["urls"] = urls
        # TODO: Remove these
        extra_info["priority_id"] = self.priority_mapping.get(
            extra_info.get("priorityName", self.default_priority)
        )
        extra_info["status_id"] = self.status_mapping.get(
            extra_info.get("statusName", self.default_status)
        )
        collected_test_case = ZephyrTestCase(
            name=name,
            project_id=self.project_id,
            folder_id=folder.id,
            **extra_info,
        )

        try:
            idx_found = self.testcases.index(collected_test_case)
        except ValueError:
            # index returns a positive number if found
            idx_found = -1

        if idx_found != -1:
            found_test_case = self.testcases[idx_found]
            # Copy values that are known only for existing test cases
            collected_test_case.id = found_test_case.id
            collected_test_case.key = found_test_case.key
            collected_test_case.jira_issues_links = found_test_case.jira_issues_links
            collected_test_case.urls_links = found_test_case.urls_links
            self._maybe_update_test_case(collected_test_case, found_test_case)
            issue_links_to_remove = set(found_test_case.jira_issues) - set(
                collected_test_case.jira_issues
            )
            issues_to_create = set(collected_test_case.jira_issues) - set(
                found_test_case.jira_issues
            )
            urls_links_to_remove = set(found_test_case.urls) - set(
                collected_test_case.urls
            )
            urls_links_to_create = set(collected_test_case.urls) - set(
                found_test_case.urls
            )
        else:
            # Test case not found
            response = self.zephyr_instance.api.test_cases.create_test_case(
                self.project_key, name, folderId=folder.id, **extra_info
            )
            collected_test_case.key = response["key"]
            collected_test_case.id = response["id"]
            issue_links_to_remove = set()
            issues_to_create = set(collected_test_case.jira_issues)
            urls_links_to_remove = set()
            urls_links_to_create = set(collected_test_case.urls)

        for issue_id in issue_links_to_remove:
            self.zephyr_instance.api.links.delete_link(
                collected_test_case.jira_issues_links[issue_id]
            )
        for issue_id in issues_to_create:
            self.zephyr_instance.api.test_cases.create_issue_links(
                collected_test_case.key, issue_id
            )
        for url in urls_links_to_remove:
            self.zephyr_instance.api.links.delete_link(
                collected_test_case.urls_links[url]
            )
        for url in urls_links_to_create:
            self.zephyr_instance.api.test_cases.create_web_links(
                collected_test_case.key, url
            )

        if isinstance(test_steps, str):
            test_steps = test_steps.replace("\n", "<br>")
            self.zephyr_instance.api.test_cases.create_test_script(
                collected_test_case.key, script_type="plain", text=test_steps
            )
        else:
            zephyr_test_steps = [
                {
                    "inline": {
                        "description": ts["step"],
                        "testData": "",
                        "expectedResult": ts.get("expected", ""),
                    }
                }
                for ts in test_steps
            ]
            self.zephyr_instance.api.test_cases.post_test_steps(
                collected_test_case.key,
                mode=TEST_STEPS_OVERWRITE,
                items=zephyr_test_steps,
            )
        self.testcases.append(collected_test_case)
        return collected_test_case.key

    def _create_folder(self, name: str, parent_id: Optional[int] = None) -> Folder:
        new_folder = self.zephyr_instance.api.folders.create_folder(
            name, self.project_key, TEST_CASE_FOLDER_TYPE, parentId=parent_id
        )
        return Folder(name, int(new_folder["id"]))

    def _mkfolders(self, path: pathlib.Path) -> Folder:
        parent_folder = self.root_folder
        for folder_name in path.parts:
            for child in parent_folder.children:
                if child.name == folder_name:
                    parent_folder = child
                    break
            else:
                new_folder = self._create_folder(folder_name, parent_folder.id)
                parent_folder.add_child(new_folder)
                # The new directory is the parent for the next iteration
                parent_folder = new_folder
        return parent_folder

    def _populate_root_folder(self, zephyr_folders_queue: queue.Queue[dict]) -> Folder:
        root_folder = Folder("root", None)
        while not zephyr_folders_queue.empty():
            folder_dict = zephyr_folders_queue.get()
            if folder_dict["folderType"] != TEST_CASE_FOLDER_TYPE:
                continue
            id = folder_dict["id"]
            name = folder_dict["name"]
            parent = folder_dict["parentId"]
            if parent:
                folder = root_folder.search_by_id(parent)
                if folder:
                    folder.add_child(Folder(name, id))
                else:
                    # Add the folder back to revisit later
                    zephyr_folders_queue.put(folder_dict)
            else:
                root_folder.add_child(Folder(name, id))
        return root_folder

    def pytest_collection(self, session: pytest.Session):
        isinstance(session, pytest.Session)

    def pytest_collection_modifyitems(
        self, session: pytest.Session, config: pytest.Config, items: List[pytest.Item]
    ):
        isinstance(session, pytest.Session)
        for item in items:
            zephyr_marker = item.get_closest_marker("zephyr_testcase")
            if zephyr_marker:
                path, name = item.nodeid.rsplit("::", maxsplit=1)
                # Handle test classes
                path = path.replace("::", os.sep)
                tmp_folder = self._mkfolders(pathlib.Path(path))
                test_case_info = zephyr_marker.kwargs
                jira_issues = test_case_info.get("jira_issues", None)
                urls = test_case_info.get("urls", None)
                test_steps = test_case_info.get("test_steps", "doc")
                # TODO: Make this prettier
                if test_steps == "doc":
                    test_steps = item.obj.__doc__ or " "  # type: ignore[attr-defined]
                test_key = self._create_test_case(
                    name, tmp_folder, jira_issues, urls, test_steps, test_case_info
                )
                # If we are not publishing, we don't need to store the test key
                if not config.option.zephyr_no_publish:
                    setattr(item, "zephyr_test_key", test_key)
        if config.option.zephyr_no_publish:
            return
        testcycle_name: str = config.getini("zephyr_testcycle_name")
        if not testcycle_name:
            testcycle_name = "Pytest run"
        testcycle_description = config.getini("zephyr_testcycle_description")
        self.executor_id = config.option.zephyr_owner_id or os.environ.get(
            "ZEPHYR_OWNER_ID"
        )
        response = self.zephyr_instance.api.test_cycles.create_test_cycle(
            project_key=self.project_key,
            name=testcycle_name,
            description=testcycle_description,
            ownerId=self.executor_id,
        )
        self.testcycle_key = response["key"]
        test_plan_id = config.getini("zephyr_testplan_id")
        if test_plan_id:
            if not test_plan_id.startswith(self.project_key):
                test_plan_id = f"{self.project_key}-{test_plan_id}"
            self.zephyr_instance.api.session.post(
                f"testplans/{test_plan_id}/links/testcycles",
                {"testCycleIdOrKey": self.testcycle_key},
            )

    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(self, item: pytest.Item, call: pytest.CallInfo):
        # Works only for test cases that zephyr knows about
        outcome = yield
        if hasattr(item, "zephyr_test_key"):
            test_report = pytest.TestReport.from_item_and_call(item, call)
            result: str = test_report.outcome
            rep = outcome.get_result()  # useful for xfail/xpass tests
            comment = test_report.longreprtext.replace("\n", "<br>")
            if hasattr(rep, "wasxfail"):
                if result == "failed":
                    result = "xfailed"
                elif result == "passed":
                    result = "xpassed"
                    comment = "Test passed unexpectedly"
            duration: float = test_report.duration
            # skipped tests are not called
            # this is the reason for the explicit check
            if result == "skipped" or test_report.when == "call":
                self.zephyr_instance.api.test_executions.create_test_execution(
                    self.project_key,
                    getattr(item, "zephyr_test_key"),
                    self.testcycle_key,
                    _result_mapping(result),
                    executedById=self.executor_id,
                    executionTime=duration * 1000,  # in milliseconds
                    comment=comment,
                )


def pytest_configure(config: pytest.Config):
    if not config.option.zephyr:
        return
    zephyr_manager = ZephyrManager._load_config_params(config)
    if zephyr_manager:
        config.pluginmanager.register(zephyr_manager)


def pytest_addoption(parser: pytest.Parser):
    parser.addoption("--zephyr", action="store_true", help="Enable Zephyr integration")
    parser.addoption(
        "--zephyr-no-publish",
        action="store_true",
        help="Do not send results to Zephyr",
        dest="zephyr_no_publish",
    )
    parser.addoption(
        "--zephyr-owner-id",
        action="store",
        dest="zephyr_owner_id",
        default=None,
        help="Zephyr owner id for creating test cycles. If not provided, it will be taken from os env vars. Otherwise, it will not be set",  # noqa: E501
    )
    parser.addini(
        "zephyr_project_key", help="[Required] JZephyr project key", type="string"
    )
    parser.addini(
        "zephyr_auth_token", help="[Required] JZephyr auth token", type="string"
    )
    parser.addini(
        "zephyr_strict",
        help="Whether to raise an error (True) or issue a warning (False) if Zephyr is not available. Default False",  # noqa: E501
        type="bool",
    )
    parser.addini(
        "zephyr_jira_base_url",
        help="[Required] JJira base url for Jira interaction",
        type="string",
    )
    parser.addini(
        "zephyr_jira_email",
        help="[Required] JJira email for Jira interaction",
        type="string",
    )
    parser.addini(
        "zephyr_jira_token",
        help="[Required] Jira auth token for Jira interaction",
        type="string",
    )
    parser.addini(
        "zephyr_testcycle_name", help="[Required] Zephyr test cycle name", type="string"
    )
    parser.addini(
        "zephyr_testcycle_description",
        help="Zephyr test cycle description",
        type="string",
    )
    parser.addini(
        "zephyr_testplan_id",
        help="Zephyr test plan to link the newly created test cycle to",
        type="string",
    )
