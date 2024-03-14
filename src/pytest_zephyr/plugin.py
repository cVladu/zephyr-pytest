# -*- coding: utf-8 -*-
import os
import pathlib
import queue
from typing import Any, List, Mapping, Optional, Dict

import pytest
from pytest import PytestConfigWarning
from zephyr import API_V2, ZephyrScale  # type: ignore[import]

from ._jira_integration import Jira
from .zephyr_interface.zephyr_folder_structure import TEST_CASE_FOLDER_TYPE, Folder
from .zephyr_interface.zephyr_test_case import ZephyrTestCase, TEST_STEPS_OVERWRITE


def _fmt_zephyr_error(msg: str):
    return RuntimeError(f"zephyr: {msg}")


def _result_mapping(result: str) -> str:
    return {
        "passed": "Pass",
        "failed": "Fail",
        "skipped": "Not Executed",
        "xfailed": "Blocked",
        "xpassed": "Fail",
    }[result]


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
        except Exception as reason:
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
        self.project_id = self.zephyr_instance.api.projects.get_project(
            self.project_key
        )["id"]
        self.testcases: List[ZephyrTestCase] = self._get_all_testscases()
        zephyr_folders = self.zephyr_instance.api.folders.get_folders()
        folders_queue: queue.Queue[dict] = queue.Queue()
        for folder in zephyr_folders:
            folders_queue.put(folder)
        self.root_folder = self._populate_root_folder(folders_queue)
        self.jira_instance = Jira(jira_base_url, jira_email, jira_token)
        self.testcycle_key = None
        self.owner_id: "str | None" = None

    def _get_all_testscases(self) -> List[ZephyrTestCase]:
        ret: List[ZephyrTestCase] = []
        zephyr_testcases = self.zephyr_instance.api.test_cases.get_test_cases(
            projectKey=self.project_key
        )
        for testcase_dict in zephyr_testcases:
            testcase = ZephyrTestCase(
                testcase_dict["key"],
                testcase_dict["name"],
                testcase_dict["folder"]["id"],
            )
            ret.append(testcase)
        return ret

    def _create_test_case(
        self,
        name: str,
        folder: Folder,
        jira_issues: Optional[List[str]],
        urls: Optional[List[str]],
        test_steps: "List[Dict[str, str]] | str",
        extra_info: Mapping[str, Any],
    ) -> str:
        # We do not care about key when searching
        if ZephyrTestCase("", name, folder.id) in self.testcases:
            idx_found = self.testcases.index(ZephyrTestCase("", name, folder.id))
            return self.testcases[idx_found].key

        new_test_case = self.zephyr_instance.api.test_cases.create_test_case(
            self.project_key, name, folderId=folder.id, **extra_info
        )
        test_case_key: str = new_test_case["key"]
        if not jira_issues:
            jira_issues = []
        if not urls:
            urls = []
        for jira_issue in jira_issues:
            if jira_issue.isnumeric():
                jira_issue = f"{self.project_key}-{jira_issue}"
            jira_issue_id = self.jira_instance.get_issue_id(jira_issue)
            self.zephyr_instance.api.test_cases.create_issue_links(
                test_case_key, jira_issue_id
            )
        for url in urls:
            self.zephyr_instance.api.test_cases.create_web_links(test_case_key, url)
        if isinstance(test_steps, str):
            test_steps = test_steps.replace("\n", "<br>")
            self.zephyr_instance.api.test_cases.create_test_script(
                test_case_key, script_type="plain", text=test_steps
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
                test_case_key, mode=TEST_STEPS_OVERWRITE, items=zephyr_test_steps
            )
        self.testcases.append(ZephyrTestCase(test_case_key, name, folder.id))
        return test_case_key

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
        if config.option.zephyr_no_publish:
            return
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
                setattr(item, "zephyr_test_key", test_key)
        testcycle_name: str = config.getini("zephyr_testcycle_name")
        if not testcycle_name:
            testcycle_name = "Pytest run"
        testcycle_description = config.getini("zephyr_testcycle_description")
        self.owner_id = config.option.zephyr_owner_id or os.environ.get(
            "ZEPHYR_OWNER_ID"
        )
        response = self.zephyr_instance.api.test_cycles.create_test_cycle(
            project_key=self.project_key,
            name=testcycle_name,
            description=testcycle_description,
            ownerId=self.owner_id,
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
                    executedById=self.owner_id,
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
