# -*- coding: utf-8 -*-
import pytest
import json
import pytest_mock

pytest_plugins = "pytester"
pytest_example_dir = "examples"


@pytest.fixture(scope="session")
def config_tokens():
    with open("config_tokens.json", "r") as f:
        yield json.load(f)


@pytest.fixture
def mock_jira(monkeypatch: pytest.MonkeyPatch):
    def get_issue_id(self, issue_str):
        return int(issue_str.split("-")[1])

    monkeypatch.setattr(
        "pytest_zephyr._jira_integration.Jira.get_issue_id", get_issue_id
    )


@pytest.fixture(scope="function")
def mock_zephyr(mocker: pytest_mock.MockerFixture):

    mocker.patch(
        "zephyr.scale.cloud.endpoints.projects.ProjectEndpoints.get_project",
        return_value={"id": 1},
    )

    mocker.patch(
        "zephyr.scale.cloud.endpoints.folders.FolderEndpoints.get_folders",
        return_value=[],
    )
    mocker.patch(
        "zephyr.scale.cloud.endpoints.priorities.PriorityEndpoints.get_priorities",
        return_value=[
            {"name": "Low", "id": 1, "default": False},
            {"name": "Medium", "id": 2, "default": True},
            {"name": "High", "id": 3, "default": False},
        ],
    )
    mocker.patch(
        "zephyr.scale.cloud.endpoints.statuses.StatusEndpoints.get_statuses",
        return_value=[
            {"name": "Draft", "id": 1, "default": True},
            {"name": "Approved", "id": 2, "default": False},
            {"name": "Obsolete", "id": 3, "default": False},
        ],
    )
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[],
    )

    update_test_case = mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.update_test_case"
    )

    create_test_case = mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.create_test_case"
    )

    create_test_script = mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.create_test_script"
    )

    create_test_steps = mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.post_test_steps"
    )

    delete_link = mocker.patch(
        "zephyr.scale.cloud.endpoints.links.LinkEndpoints.delete_link"
    )

    create_issue_link = mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.create_issue_links"
    )

    create_web_link = mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.create_web_links"
    )

    create_folder = mocker.patch(
        "zephyr.scale.cloud.endpoints.folders.FolderEndpoints.create_folder",
        return_value={"id": 100},
    )

    create_test_cycle = mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cycles.TestCycleEndpoints.create_test_cycle"
    )

    create_test_execution = mocker.patch(
        "zephyr.scale.cloud.endpoints.test_executions.TestExecutionEndpoints.create_test_execution"
    )

    class TestCases:
        def __init__(self):
            self.create_test_case = create_test_case
            self.update_test_case = update_test_case
            self.create_test_script = create_test_script
            self.create_test_steps = create_test_steps

    class Links:
        def __init__(self):
            self.create_issue_link = create_issue_link
            self.create_web_link = create_web_link
            self.delete_link = delete_link

    class Folders:
        def __init__(self):
            self.create_folder = create_folder

    class Executions:
        def __init__(self):
            self.create_test_cycle = create_test_cycle
            self.create_test_execution = create_test_execution

    class ZephyrMock:
        def __init__(self):
            self.test_cases = TestCases()
            self.links = Links()
            self.folders = Folders()
            self.executions = Executions()

    return ZephyrMock()
