from requests.exceptions import HTTPError
from typing import Any, Mapping, Optional
from datetime import timedelta
import os
import queue
import pathlib
import json
import pytest
from pytest import PytestConfigWarning, PytestCollectionWarning
from zephyr import ZephyrScale, API_V2
from .zephyr_interface.zephyr_test_case import ZephyrTestCase
from .zephyr_interface.zephyr_folder_structure import Folder, TEST_CASE_FOLDER_TYPE
from ._jira_integration import Jira

def _fmt_zephyr_error(msg: str):
    return ValueError(f"zephyr: {msg}")

class ZephyrManager:
    
    @classmethod
    def _load_config_params(cls, config: pytest.Config) -> "ZephyrManager | None":
        kwargs = {}
        mandatory_params = ["zephyr_auth_token",
                            "zephyr_project_key", 
                            "zephyr_jira_base_url", 
                            "zephyr_jira_email", 
                            "zephyr_jira_token"]
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
            raise _fmt_zephyr_error(f"The following mandatory params not found in pytest ini file or sys env vars:\n"
                                    f"{', '.join(mandatory_absent)}\n"
                                    f"See README for list of parameters and their use.")
        # Check connection
        strict = config.getini("zephyr_strict") or False
        healthy = True
        error_string = ""
        zephyr_manager = None
        try:
            zephyr_manager = cls(**kwargs)
        except Exception as reason:
            healthy = False
            error_string = f"Could not connect to Zephyr. Reason: {reason}"
        if not healthy:
            if strict:
                raise _fmt_zephyr_error(error_string)
            else:
                config.issue_config_time_warning(PytestConfigWarning(error_string), stacklevel=2)
        return zephyr_manager

    def __init__(self, auth_token: str, project_key: str, jira_base_url: str, jira_email: str, jira_token: str):
        self.zephyr_instance: ZephyrScale = ZephyrScale(token=auth_token, api_version=API_V2)
        self.project_key = project_key
        self.testcases = []
        self.project_id = self.zephyr_instance.api.projects.get_project(self.project_key)["id"]
        zephyr_folders = self.zephyr_instance.api.folders.get_folders()
        folders_queue = queue.Queue()
        for folder in zephyr_folders:
            folders_queue.put(folder)
        self.root_folder = self._populate_root_folder(folders_queue)
        self.jira_instance = Jira(jira_base_url, jira_email, jira_token)

    def _create_folder(self, name: str, parent_id: int | None = None) -> Folder:
        new_folder = self.zephyr_instance.api.folders.create_folder(name, self.project_key, TEST_CASE_FOLDER_TYPE, parentId=parent_id)
        return Folder(name, int(new_folder["id"]))

    def _create_test_case(self, 
                          name: str, 
                          folder: Folder, 
                          jira_issues: Optional[list[str]], 
                          urls: Optional[list[str]], 
                          test_steps: Optional[list[str] | str], 
                          extra_info: Mapping[str, Any]) -> ZephyrTestCase | None:
        new_test_case = self.zephyr_instance.api.test_cases.create_test_case(self.project_key, name, folderId=folder.id, **extra_info)
        test_case_key = new_test_case["key"]
        if not jira_issues:
            jira_issues = []
        if not urls:
            urls = []
        for jira_issue in jira_issues:
            if jira_issue.isnumeric():
                jira_issue = f"{self.project_key}-{jira_issue}"
            jira_issue_id = self.jira_instance.get_issue_id(jira_issue)
            self.zephyr_instance.api.test_cases.create_issue_links(test_case_key, jira_issue_id)
        for url in urls:
            self.zephyr_instance.api.test_cases.create_web_links(test_case_key, url)
        if isinstance(test_steps, str):
            test_steps = test_steps.replace("\n", "<br>")
            self.zephyr_instance.api.test_cases.create_test_script(test_case_key, script_type="plain", text=test_steps) 
        else:
            pass
            # self.zephyr_instance.api.test_cases.post_test_steps(test_case_key, mode="OVERWRITE", steps=test_steps)
        return None

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

    def pytest_collection_modifyitems(self, session: pytest.Session, config: pytest.Config, items: list[pytest.Item]):
        isinstance(session, pytest.Session)
        isinstance(config, pytest.Config)
        isinstance(items, list)

    def pytest_runtest_setup(self, item: pytest.Item):
        zephyr_marker = item.get_closest_marker("zephyr_testcase")
        if zephyr_marker:
            path, name = item.nodeid.rsplit("::", maxsplit=1)
            # Handle test classes
            path = path.replace("::", os.sep)
            tmp_folder = self._mkfolders(pathlib.Path(path))
            test_case_info = zephyr_marker.kwargs
            jira_issues = test_case_info.get("jira_issues", None)
            urls = test_case_info.get("urls", None)
            test_steps = test_case_info.get("test_steps", [])
            # TODO: Make this prettier
            if test_steps == "doc":
                test_steps = item.obj.__doc__
            self._create_test_case(name, tmp_folder, jira_issues, urls, test_steps, test_case_info)
        else:
            print("No Zephyr marker")

def pytest_configure(config: pytest.Config):
    if not config.option.zephyr:
        return
    zephyr_manager = ZephyrManager._load_config_params(config)
    if zephyr_manager:
        config.pluginmanager.register(zephyr_manager)

    
def pytest_addoption(parser):
    parser.addoption("--zephyr", action="store_true", help="Enable Zephyr integration")
    parser.addini("zephyr_project_key", help="Zephyr project key", type="string")
    parser.addini("zephyr_auth_token", help="Zephyr auth token", type="string")
    parser.addini("zephyr_strict", help="Whether to raise an error (True) or issue a warning (False) if Zephyr is not available. Default False", type="bool")
    parser.addini("zephyr_jira_base_url", help="Jira base url for Jira interaction", type="string")
    parser.addini("zephyr_jira_email", help="Jira email for Jira interaction", type="string")
    parser.addini("zephyr_jira_token", help="Jira auth token for Jira interaction", type="string")

