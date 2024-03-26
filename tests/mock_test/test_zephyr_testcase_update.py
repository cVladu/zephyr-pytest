# -*- coding: utf-8 -*-
import pytest


def test_zephyr_update_testcase_objective_change(pytester, mock_zephyr, mocker):
    """
    Check that the plugin updates the test case objective.
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.folders.FolderEndpoints.get_folders",
        return_value=[
            {
                "id": 100,
                "folderType": "TEST_CASE",
                "name": "test_zephyr_update_testcase_objective_change.py",
                "parentId": None,
            }
        ],
    )
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "objective": "Test objective original",
                "precondition": "Test Precondition",
                "estimatedTime": 123,
                "labels": ["a_label", "b_label"],
                "priority": {"id": 3, "self": "linkpriority/3"},
                "status": {"id": 3, "self": "linkstatus/3"},
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {"accountId": "owner123", "self": "linkuser/owner123"},
                "customFields": {"custom_field": "custom_value"},
                "links": {"self": "linktestcase/5", "issues": [], "webLinks": []},
            }
        ],
    )
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
"""
    )
    pytester.makepyfile(
        """
                        import pytest

                        @pytest.mark.zephyr_testcase(objective="Test Objective Updated",
                                                     precondition="Test Precondition",
                                                     estimatedTime=123,
                                                     priorityName="High",
                                                     statusName="Obsolete",
                                                     ownerId="owner123",
                                                     labels=["a_label", "b_label"],
                                                     customFields={"custom_field": "custom_value"})
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.test_cases.create_test_case.call_count == 0
    mocked_api.test_cases.update_test_case.assert_called_once_with(
        test_case_id=5,
        id=5,
        test_case_key="ANY-T5",
        key="ANY-T5",
        name="test_sth",
        createdOn="",
        project_id=1,
        objective="Test Objective Updated",
        precondition="Test Precondition",
        estimatedTime=123,
        labels=["a_label", "b_label"],
        priority_id=3,
        status_id=3,
        folder={"id": 100},
        owner={"accountId": "owner123"},
        jira_issues=[],
        urls=[],
        customFields={"custom_field": "custom_value"},
    )


def test_zephyr_update_testcase_objective_remove(pytester, mock_zephyr, mocker):
    """
    Check that the plugin removes the test case objective.
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.folders.FolderEndpoints.get_folders",
        return_value=[
            {
                "id": 100,
                "folderType": "TEST_CASE",
                "name": "test_zephyr_update_testcase_objective_remove.py",
                "parentId": None,
            }
        ],
    )
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "objective": "Test objective original",
                "precondition": "Test Precondition",
                "estimatedTime": 123,
                "labels": ["a_label", "b_label"],
                "priority": {"id": 3, "self": "linkpriority/3"},
                "status": {"id": 3, "self": "linkstatus/3"},
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {"accountId": "owner123", "self": "linkuser/owner123"},
                "customFields": {"custom_field": "custom_value"},
                "links": {"self": "linktestcase/5", "issues": [], "webLinks": []},
            }
        ],
    )
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
"""
    )
    pytester.makepyfile(
        """
                        import pytest

                        @pytest.mark.zephyr_testcase(precondition="Test Precondition",
                                                     estimatedTime=123,
                                                     priorityName="High",
                                                     statusName="Obsolete",
                                                     ownerId="owner123",
                                                     labels=["a_label", "b_label"],
                                                     customFields={"custom_field": "custom_value"})
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.test_cases.create_test_case.call_count == 0
    mocked_api.test_cases.update_test_case.assert_called_once_with(
        test_case_id=5,
        id=5,
        test_case_key="ANY-T5",
        key="ANY-T5",
        name="test_sth",
        createdOn="",
        project_id=1,
        objective="",
        precondition="Test Precondition",
        estimatedTime=123,
        labels=["a_label", "b_label"],
        priority_id=3,
        status_id=3,
        folder={"id": 100},
        owner={"accountId": "owner123"},
        jira_issues=[],
        urls=[],
        customFields={"custom_field": "custom_value"},
    )


def test_zephyr_update_testcase_objective_add(pytester, mock_zephyr, mocker):
    """
    Check that the plugin adds the test case objective.
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.folders.FolderEndpoints.get_folders",
        return_value=[
            {
                "id": 100,
                "folderType": "TEST_CASE",
                "name": "test_zephyr_update_testcase_objective_add.py",
                "parentId": None,
            }
        ],
    )
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "objective": "",
                "precondition": "Test Precondition",
                "estimatedTime": 123,
                "labels": ["a_label", "b_label"],
                "priority": {"id": 3, "self": "linkpriority/3"},
                "status": {"id": 3, "self": "linkstatus/3"},
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {"accountId": "owner123", "self": "linkuser/owner123"},
                "customFields": {"custom_field": "custom_value"},
                "links": {"self": "linktestcase/5", "issues": [], "webLinks": []},
            }
        ],
    )
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
"""
    )
    pytester.makepyfile(
        """
                        import pytest

                        @pytest.mark.zephyr_testcase(objective="Test Objective Added",
                                                     precondition="Test Precondition",
                                                     estimatedTime=123,
                                                     priorityName="High",
                                                     statusName="Obsolete",
                                                     ownerId="owner123",
                                                     labels=["a_label", "b_label"],
                                                     customFields={"custom_field": "custom_value"})
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.test_cases.create_test_case.call_count == 0
    mocked_api.test_cases.update_test_case.assert_called_once_with(
        test_case_id=5,
        id=5,
        test_case_key="ANY-T5",
        key="ANY-T5",
        name="test_sth",
        createdOn="",
        project_id=1,
        objective="Test Objective Added",
        precondition="Test Precondition",
        estimatedTime=123,
        labels=["a_label", "b_label"],
        priority_id=3,
        status_id=3,
        folder={"id": 100},
        owner={"accountId": "owner123"},
        jira_issues=[],
        urls=[],
        customFields={"custom_field": "custom_value"},
    )


def test_zephyr_update_testcase_precondition_change(pytester, mock_zephyr, mocker):
    """
    Check that the plugin updates the test case precondition.
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.folders.FolderEndpoints.get_folders",
        return_value=[
            {
                "id": 100,
                "folderType": "TEST_CASE",
                "name": "test_zephyr_update_testcase_precondition_change.py",
                "parentId": None,
            }
        ],
    )
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "objective": "Test objective",
                "precondition": "Test Precondition Original",
                "estimatedTime": 123,
                "labels": ["a_label", "b_label"],
                "priority": {"id": 3, "self": "linkpriority/3"},
                "status": {"id": 3, "self": "linkstatus/3"},
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {"accountId": "owner123", "self": "linkuser/owner123"},
                "customFields": {"custom_field": "custom_value"},
                "links": {"self": "linktestcase/5", "issues": [], "webLinks": []},
            }
        ],
    )
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
"""
    )
    pytester.makepyfile(
        """
                        import pytest

                        @pytest.mark.zephyr_testcase(objective="Test Objective",
                                                     precondition="Test Precondition Updated",
                                                     estimatedTime=123,
                                                     priorityName="High",
                                                     statusName="Obsolete",
                                                     ownerId="owner123",
                                                     labels=["a_label", "b_label"],
                                                     customFields={"custom_field": "custom_value"})
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.test_cases.create_test_case.call_count == 0
    mocked_api.test_cases.update_test_case.assert_called_once_with(
        test_case_id=5,
        id=5,
        test_case_key="ANY-T5",
        key="ANY-T5",
        name="test_sth",
        createdOn="",
        project_id=1,
        objective="Test Objective",
        precondition="Test Precondition Updated",
        estimatedTime=123,
        labels=["a_label", "b_label"],
        priority_id=3,
        status_id=3,
        folder={"id": 100},
        owner={"accountId": "owner123"},
        jira_issues=[],
        urls=[],
        customFields={"custom_field": "custom_value"},
    )


def test_zephyr_update_testcase_precondition_remove(pytester, mock_zephyr, mocker):
    """
    Check that the plugin removes the test case precondition.
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.folders.FolderEndpoints.get_folders",
        return_value=[
            {
                "id": 100,
                "folderType": "TEST_CASE",
                "name": "test_zephyr_update_testcase_precondition_remove.py",
                "parentId": None,
            }
        ],
    )
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "objective": "Test objective",
                "precondition": "Test Precondition Original",
                "estimatedTime": 123,
                "labels": ["a_label", "b_label"],
                "priority": {"id": 3, "self": "linkpriority/3"},
                "status": {"id": 3, "self": "linkstatus/3"},
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {"accountId": "owner123", "self": "linkuser/owner123"},
                "customFields": {"custom_field": "custom_value"},
                "links": {"self": "linktestcase/5", "issues": [], "webLinks": []},
            }
        ],
    )
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
"""
    )
    pytester.makepyfile(
        """
                        import pytest

                        @pytest.mark.zephyr_testcase(objective="Test objective",
                                                     estimatedTime=123,
                                                     priorityName="High",
                                                     statusName="Obsolete",
                                                     ownerId="owner123",
                                                     labels=["a_label", "b_label"],
                                                     customFields={"custom_field": "custom_value"})
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.test_cases.create_test_case.call_count == 0
    mocked_api.test_cases.update_test_case.assert_called_once_with(
        test_case_id=5,
        id=5,
        test_case_key="ANY-T5",
        key="ANY-T5",
        name="test_sth",
        createdOn="",
        project_id=1,
        objective="Test objective",
        precondition="",
        estimatedTime=123,
        labels=["a_label", "b_label"],
        priority_id=3,
        status_id=3,
        folder={"id": 100},
        owner={"accountId": "owner123"},
        jira_issues=[],
        urls=[],
        customFields={"custom_field": "custom_value"},
    )


def test_zephyr_update_testcase_precondition_add(pytester, mock_zephyr, mocker):
    """
    Check that the plugin adds the test case precondition.
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.folders.FolderEndpoints.get_folders",
        return_value=[
            {
                "id": 100,
                "folderType": "TEST_CASE",
                "name": "test_zephyr_update_testcase_precondition_add.py",
                "parentId": None,
            }
        ],
    )
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "objective": "Test Objective",
                "precondition": "",
                "estimatedTime": 123,
                "labels": ["a_label", "b_label"],
                "priority": {"id": 3, "self": "linkpriority/3"},
                "status": {"id": 3, "self": "linkstatus/3"},
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {"accountId": "owner123", "self": "linkuser/owner123"},
                "customFields": {"custom_field": "custom_value"},
                "links": {"self": "linktestcase/5", "issues": [], "webLinks": []},
            }
        ],
    )
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
"""
    )
    pytester.makepyfile(
        """
                        import pytest

                        @pytest.mark.zephyr_testcase(objective="Test Objective",
                                                     precondition="Test Precondition Added",
                                                     estimatedTime=123,
                                                     priorityName="High",
                                                     statusName="Obsolete",
                                                     ownerId="owner123",
                                                     labels=["a_label", "b_label"],
                                                     customFields={"custom_field": "custom_value"})
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.test_cases.create_test_case.call_count == 0
    mocked_api.test_cases.update_test_case.assert_called_once_with(
        test_case_id=5,
        id=5,
        test_case_key="ANY-T5",
        key="ANY-T5",
        name="test_sth",
        createdOn="",
        project_id=1,
        objective="Test Objective",
        precondition="Test Precondition Added",
        estimatedTime=123,
        labels=["a_label", "b_label"],
        priority_id=3,
        status_id=3,
        folder={"id": 100},
        owner={"accountId": "owner123"},
        jira_issues=[],
        urls=[],
        customFields={"custom_field": "custom_value"},
    )


def test_zephyr_update_testcase_estimatedtime_change(pytester, mock_zephyr, mocker):
    """
    Check that the plugin updates the test case estimated time.
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.folders.FolderEndpoints.get_folders",
        return_value=[
            {
                "id": 100,
                "folderType": "TEST_CASE",
                "name": "test_zephyr_update_testcase_estimatedtime_change.py",
                "parentId": None,
            }
        ],
    )
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "objective": "Test objective",
                "precondition": "Test Precondition",
                "estimatedTime": 100,
                "labels": ["a_label", "b_label"],
                "priority": {"id": 3, "self": "linkpriority/3"},
                "status": {"id": 3, "self": "linkstatus/3"},
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {"accountId": "owner123", "self": "linkuser/owner123"},
                "customFields": {"custom_field": "custom_value"},
                "links": {"self": "linktestcase/5", "issues": [], "webLinks": []},
            }
        ],
    )
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
"""
    )
    pytester.makepyfile(
        """
                        import pytest

                        @pytest.mark.zephyr_testcase(objective="Test Objective",
                                                     precondition="Test Precondition",
                                                     estimatedTime=123,
                                                     priorityName="High",
                                                     statusName="Obsolete",
                                                     ownerId="owner123",
                                                     labels=["a_label", "b_label"],
                                                     customFields={"custom_field": "custom_value"})
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.test_cases.create_test_case.call_count == 0
    mocked_api.test_cases.update_test_case.assert_called_once_with(
        test_case_id=5,
        id=5,
        test_case_key="ANY-T5",
        key="ANY-T5",
        name="test_sth",
        createdOn="",
        project_id=1,
        objective="Test Objective",
        precondition="Test Precondition",
        estimatedTime=123,
        labels=["a_label", "b_label"],
        priority_id=3,
        status_id=3,
        folder={"id": 100},
        owner={"accountId": "owner123"},
        jira_issues=[],
        urls=[],
        customFields={"custom_field": "custom_value"},
    )


def test_zephyr_update_testcase_estimatedtime_remove(pytester, mock_zephyr, mocker):
    """
    Check that the plugin removes the test case estimated time.
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.folders.FolderEndpoints.get_folders",
        return_value=[
            {
                "id": 100,
                "folderType": "TEST_CASE",
                "name": "test_zephyr_update_testcase_estimatedtime_remove.py",
                "parentId": None,
            }
        ],
    )
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "objective": "Test objective",
                "precondition": "Test Precondition Original",
                "estimatedTime": 123,
                "labels": ["a_label", "b_label"],
                "priority": {"id": 3, "self": "linkpriority/3"},
                "status": {"id": 3, "self": "linkstatus/3"},
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {"accountId": "owner123", "self": "linkuser/owner123"},
                "customFields": {"custom_field": "custom_value"},
                "links": {"self": "linktestcase/5", "issues": [], "webLinks": []},
            }
        ],
    )
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
"""
    )
    pytester.makepyfile(
        """
                        import pytest

                        @pytest.mark.zephyr_testcase(objective="Test objective",
                                                     precondition="Test Precondition",
                                                     priorityName="High",
                                                     statusName="Obsolete",
                                                     ownerId="owner123",
                                                     labels=["a_label", "b_label"],
                                                     customFields={"custom_field": "custom_value"})
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.test_cases.create_test_case.call_count == 0
    mocked_api.test_cases.update_test_case.assert_called_once_with(
        test_case_id=5,
        id=5,
        test_case_key="ANY-T5",
        key="ANY-T5",
        name="test_sth",
        createdOn="",
        project_id=1,
        objective="Test objective",
        precondition="Test Precondition",
        estimatedTime=0,
        labels=["a_label", "b_label"],
        priority_id=3,
        status_id=3,
        folder={"id": 100},
        owner={"accountId": "owner123"},
        jira_issues=[],
        urls=[],
        customFields={"custom_field": "custom_value"},
    )


def test_zephyr_update_testcase_estimatedtime_add(pytester, mock_zephyr, mocker):
    """
    Check that the plugin adds the test case estimated time.
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.folders.FolderEndpoints.get_folders",
        return_value=[
            {
                "id": 100,
                "folderType": "TEST_CASE",
                "name": "test_zephyr_update_testcase_estimatedtime_add.py",
                "parentId": None,
            }
        ],
    )
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "objective": "Test Objective",
                "precondition": "",
                "estimatedTime": None,
                "labels": ["a_label", "b_label"],
                "priority": {"id": 3, "self": "linkpriority/3"},
                "status": {"id": 3, "self": "linkstatus/3"},
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {"accountId": "owner123", "self": "linkuser/owner123"},
                "customFields": {"custom_field": "custom_value"},
                "links": {"self": "linktestcase/5", "issues": [], "webLinks": []},
            }
        ],
    )
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
"""
    )
    pytester.makepyfile(
        """
                        import pytest

                        @pytest.mark.zephyr_testcase(objective="Test Objective",
                                                     precondition="Test Precondition",
                                                     estimatedTime=123,
                                                     priorityName="High",
                                                     statusName="Obsolete",
                                                     ownerId="owner123",
                                                     labels=["a_label", "b_label"],
                                                     customFields={"custom_field": "custom_value"})
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.test_cases.create_test_case.call_count == 0
    mocked_api.test_cases.update_test_case.assert_called_once_with(
        test_case_id=5,
        id=5,
        test_case_key="ANY-T5",
        key="ANY-T5",
        name="test_sth",
        createdOn="",
        project_id=1,
        objective="Test Objective",
        precondition="Test Precondition",
        estimatedTime=123,
        labels=["a_label", "b_label"],
        priority_id=3,
        status_id=3,
        folder={"id": 100},
        owner={"accountId": "owner123"},
        jira_issues=[],
        urls=[],
        customFields={"custom_field": "custom_value"},
    )


def test_zephyr_update_testcase_ownerid_change(pytester, mock_zephyr, mocker):
    """
    Check that the plugin updates the test case owner id.
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.folders.FolderEndpoints.get_folders",
        return_value=[
            {
                "id": 100,
                "folderType": "TEST_CASE",
                "name": "test_zephyr_update_testcase_ownerid_change.py",
                "parentId": None,
            }
        ],
    )
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "objective": "Test objective",
                "precondition": "Test Precondition",
                "estimatedTime": 123,
                "labels": ["a_label", "b_label"],
                "priority": {"id": 3, "self": "linkpriority/3"},
                "status": {"id": 3, "self": "linkstatus/3"},
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {"accountId": "owner123", "self": "linkuser/owner123"},
                "customFields": {"custom_field": "custom_value"},
                "links": {"self": "linktestcase/5", "issues": [], "webLinks": []},
            }
        ],
    )
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
"""
    )
    pytester.makepyfile(
        """
                        import pytest

                        @pytest.mark.zephyr_testcase(objective="Test Objective",
                                                     precondition="Test Precondition",
                                                     estimatedTime=123,
                                                     priorityName="High",
                                                     statusName="Obsolete",
                                                     ownerId="owner100",
                                                     labels=["a_label", "b_label"],
                                                     customFields={"custom_field": "custom_value"})
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.test_cases.create_test_case.call_count == 0
    mocked_api.test_cases.update_test_case.assert_called_once_with(
        test_case_id=5,
        id=5,
        test_case_key="ANY-T5",
        key="ANY-T5",
        name="test_sth",
        createdOn="",
        project_id=1,
        objective="Test Objective",
        precondition="Test Precondition",
        estimatedTime=123,
        labels=["a_label", "b_label"],
        priority_id=3,
        status_id=3,
        folder={"id": 100},
        owner={"accountId": "owner100"},
        jira_issues=[],
        urls=[],
        customFields={"custom_field": "custom_value"},
    )


def test_zephyr_update_testcase_ownerid_remove(pytester, mock_zephyr, mocker):
    """
    Check that the plugin removes the test case owner id.
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.folders.FolderEndpoints.get_folders",
        return_value=[
            {
                "id": 100,
                "folderType": "TEST_CASE",
                "name": "test_zephyr_update_testcase_ownerid_remove.py",
                "parentId": None,
            }
        ],
    )
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "objective": "Test objective",
                "precondition": "Test Precondition Original",
                "estimatedTime": 123,
                "labels": ["a_label", "b_label"],
                "priority": {"id": 3, "self": "linkpriority/3"},
                "status": {"id": 3, "self": "linkstatus/3"},
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {"accountId": "owner123", "self": "linkuser/owner123"},
                "customFields": {"custom_field": "custom_value"},
                "links": {"self": "linktestcase/5", "issues": [], "webLinks": []},
            }
        ],
    )
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
"""
    )
    pytester.makepyfile(
        """
                        import pytest

                        @pytest.mark.zephyr_testcase(objective="Test objective",
                                                     precondition="Test Precondition",
                                                     estimatedTime=123,
                                                     priorityName="High",
                                                     statusName="Obsolete",
                                                     labels=["a_label", "b_label"],
                                                     customFields={"custom_field": "custom_value"})
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.test_cases.create_test_case.call_count == 0
    mocked_api.test_cases.update_test_case.assert_called_once_with(
        test_case_id=5,
        id=5,
        test_case_key="ANY-T5",
        key="ANY-T5",
        name="test_sth",
        createdOn="",
        project_id=1,
        objective="Test objective",
        precondition="Test Precondition",
        estimatedTime=123,
        labels=["a_label", "b_label"],
        priority_id=3,
        status_id=3,
        folder={"id": 100},
        jira_issues=[],
        urls=[],
        customFields={"custom_field": "custom_value"},
    )


def test_zephyr_update_testcase_ownerid_add(pytester, mock_zephyr, mocker):
    """
    Check that the plugin adds the test case owner id.
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.folders.FolderEndpoints.get_folders",
        return_value=[
            {
                "id": 100,
                "folderType": "TEST_CASE",
                "name": "test_zephyr_update_testcase_ownerid_add.py",
                "parentId": None,
            }
        ],
    )
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "objective": "Test Objective",
                "precondition": "",
                "estimatedTime": 123,
                "labels": ["a_label", "b_label"],
                "priority": {"id": 3, "self": "linkpriority/3"},
                "status": {"id": 3, "self": "linkstatus/3"},
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {},
                "customFields": {"custom_field": "custom_value"},
                "links": {"self": "linktestcase/5", "issues": [], "webLinks": []},
            }
        ],
    )
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
"""
    )
    pytester.makepyfile(
        """
                        import pytest

                        @pytest.mark.zephyr_testcase(objective="Test Objective",
                                                     precondition="Test Precondition",
                                                     estimatedTime=123,
                                                     priorityName="High",
                                                     statusName="Obsolete",
                                                     ownerId="owner123",
                                                     labels=["a_label", "b_label"],
                                                     customFields={"custom_field": "custom_value"})
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.test_cases.create_test_case.call_count == 0
    mocked_api.test_cases.update_test_case.assert_called_once_with(
        test_case_id=5,
        id=5,
        test_case_key="ANY-T5",
        key="ANY-T5",
        name="test_sth",
        createdOn="",
        project_id=1,
        objective="Test Objective",
        precondition="Test Precondition",
        estimatedTime=123,
        labels=["a_label", "b_label"],
        priority_id=3,
        status_id=3,
        folder={"id": 100},
        owner={"accountId": "owner123"},
        jira_issues=[],
        urls=[],
        customFields={"custom_field": "custom_value"},
    )


@pytest.mark.parametrize("original_priority_id", [1, 2, 3])
@pytest.mark.parametrize(
    "new_priority_name, new_priority_id", [("High", 3), ("Medium", 2), ("Low", 1)]
)
def test_zephyr_update_testcase_priority_change(
    pytester,
    mock_zephyr,
    mocker,
    original_priority_id,
    new_priority_name,
    new_priority_id,
):
    """
    Check that the plugin updates the test case priority.
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.folders.FolderEndpoints.get_folders",
        return_value=[
            {
                "id": 100,
                "folderType": "TEST_CASE",
                "name": "test_zephyr_update_testcase_priority_change.py",
                "parentId": None,
            }
        ],
    )
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "objective": "Test objective",
                "precondition": "Test Precondition",
                "estimatedTime": 123,
                "labels": ["a_label", "b_label"],
                "priority": {
                    "id": original_priority_id,
                    "self": f"linkpriority/{original_priority_id}",
                },
                "status": {"id": 3, "self": "linkstatus/3"},
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {"accountId": "owner123", "self": "linkuser/owner123"},
                "customFields": {"custom_field": "custom_value"},
                "links": {"self": "linktestcase/5", "issues": [], "webLinks": []},
            }
        ],
    )
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
"""
    )
    pytester.makepyfile(
        f"""
                        import pytest

                        @pytest.mark.zephyr_testcase(objective="Test Objective",
                                                     precondition="Test Precondition",
                                                     estimatedTime=123,
                                                     priorityName="{new_priority_name}",
                                                     statusName="Obsolete",
                                                     ownerId="owner100",
                                                     labels=["a_label", "b_label"],
                                                     customFields={{
                                                         "custom_field": "custom_value"
                                                         }})
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.test_cases.create_test_case.call_count == 0
    mocked_api.test_cases.update_test_case.assert_called_once_with(
        test_case_id=5,
        id=5,
        test_case_key="ANY-T5",
        key="ANY-T5",
        name="test_sth",
        createdOn="",
        project_id=1,
        objective="Test Objective",
        precondition="Test Precondition",
        estimatedTime=123,
        labels=["a_label", "b_label"],
        priority_id=new_priority_id,
        status_id=3,
        folder={"id": 100},
        owner={"accountId": "owner100"},
        jira_issues=[],
        urls=[],
        customFields={"custom_field": "custom_value"},
    )


@pytest.mark.parametrize("original_priority_id", [1, 2, 3])
def test_zephyr_update_testcase_priority_remove(
    pytester, mock_zephyr, mocker, original_priority_id
):
    """
    Check that the plugin removes the test case priority.
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.folders.FolderEndpoints.get_folders",
        return_value=[
            {
                "id": 100,
                "folderType": "TEST_CASE",
                "name": "test_zephyr_update_testcase_priority_remove.py",
                "parentId": None,
            }
        ],
    )
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "objective": "Test objective",
                "precondition": "Test Precondition Original",
                "estimatedTime": 123,
                "labels": ["a_label", "b_label"],
                "priority": {
                    "id": original_priority_id,
                    "self": f"linkpriority/{original_priority_id}",
                },
                "status": {"id": 3, "self": "linkstatus/3"},
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {"accountId": "owner123", "self": "linkuser/owner123"},
                "customFields": {"custom_field": "custom_value"},
                "links": {"self": "linktestcase/5", "issues": [], "webLinks": []},
            }
        ],
    )
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
"""
    )
    pytester.makepyfile(
        """
                        import pytest

                        @pytest.mark.zephyr_testcase(objective="Test objective",
                                                     precondition="Test Precondition",
                                                     estimatedTime=123,
                                                     ownerId="owner123",
                                                     statusName="Obsolete",
                                                     labels=["a_label", "b_label"],
                                                     customFields={"custom_field": "custom_value"})
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.test_cases.create_test_case.call_count == 0
    mocked_api.test_cases.update_test_case.assert_called_once_with(
        test_case_id=5,
        id=5,
        test_case_key="ANY-T5",
        key="ANY-T5",
        name="test_sth",
        createdOn="",
        project_id=1,
        objective="Test objective",
        precondition="Test Precondition",
        estimatedTime=123,
        labels=["a_label", "b_label"],
        priority_id=2,
        status_id=3,
        folder={"id": 100},
        owner={"accountId": "owner123"},
        jira_issues=[],
        urls=[],
        customFields={"custom_field": "custom_value"},
    )


@pytest.mark.parametrize(
    "new_priority_name, new_priority_id", [("High", 3), ("Medium", 2), ("Low", 1)]
)
def test_zephyr_update_testcase_priority_add(
    pytester, mock_zephyr, mocker, new_priority_name, new_priority_id
):
    """
    Check that the plugin adds the test case priority.
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.folders.FolderEndpoints.get_folders",
        return_value=[
            {
                "id": 100,
                "folderType": "TEST_CASE",
                "name": "test_zephyr_update_testcase_priority_add.py",
                "parentId": None,
            }
        ],
    )
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "objective": "Test Objective",
                "precondition": "",
                "estimatedTime": 123,
                "labels": ["a_label", "b_label"],
                "priority": {"id": 2, "self": "linkpriority/2"},
                "status": {"id": 3, "self": "linkstatus/3"},
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {},
                "customFields": {"custom_field": "custom_value"},
                "links": {"self": "linktestcase/5", "issues": [], "webLinks": []},
            }
        ],
    )
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
"""
    )
    pytester.makepyfile(
        f"""
                        import pytest

                        @pytest.mark.zephyr_testcase(objective="Test Objective",
                                                     precondition="Test Precondition",
                                                     estimatedTime=123,
                                                     priorityName="{new_priority_name}",
                                                     statusName="Obsolete",
                                                     ownerId="owner123",
                                                     labels=["a_label", "b_label"],
                                                     customFields={{
                                                         "custom_field": "custom_value"
                                                         }})
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.test_cases.create_test_case.call_count == 0
    mocked_api.test_cases.update_test_case.assert_called_once_with(
        test_case_id=5,
        id=5,
        test_case_key="ANY-T5",
        key="ANY-T5",
        name="test_sth",
        createdOn="",
        project_id=1,
        objective="Test Objective",
        precondition="Test Precondition",
        estimatedTime=123,
        labels=["a_label", "b_label"],
        priority_id=new_priority_id,
        status_id=3,
        folder={"id": 100},
        owner={"accountId": "owner123"},
        jira_issues=[],
        urls=[],
        customFields={"custom_field": "custom_value"},
    )


@pytest.mark.parametrize("original_status_id", [1, 2, 3])
@pytest.mark.parametrize(
    "new_status_name, new_status_id", [("Obsolete", 3), ("Approved", 2), ("Draft", 1)]
)
def test_zephyr_update_testcase_status_change(
    pytester,
    mock_zephyr,
    mocker,
    original_status_id,
    new_status_name,
    new_status_id,
):
    """
    Check that the plugin updates the test case status.
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.folders.FolderEndpoints.get_folders",
        return_value=[
            {
                "id": 100,
                "folderType": "TEST_CASE",
                "name": "test_zephyr_update_testcase_status_change.py",
                "parentId": None,
            }
        ],
    )
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "objective": "Test objective",
                "precondition": "Test Precondition",
                "estimatedTime": 123,
                "labels": ["a_label", "b_label"],
                "priority": {"id": 3, "self": "linkpriority/3"},
                "status": {
                    "id": {original_status_id},
                    "self": f"linkstatus/{original_status_id}",
                },
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {"accountId": "owner123", "self": "linkuser/owner123"},
                "customFields": {"custom_field": "custom_value"},
                "links": {"self": "linktestcase/5", "issues": [], "webLinks": []},
            }
        ],
    )
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
"""
    )
    pytester.makepyfile(
        f"""
                        import pytest

                        @pytest.mark.zephyr_testcase(objective="Test Objective",
                                                     precondition="Test Precondition",
                                                     estimatedTime=123,
                                                     priorityName="High",
                                                     statusName="{new_status_name}",
                                                     ownerId="owner100",
                                                     labels=["a_label", "b_label"],
                                                     customFields={{
                                                         "custom_field": "custom_value"
                                                         }})
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.test_cases.create_test_case.call_count == 0
    mocked_api.test_cases.update_test_case.assert_called_once_with(
        test_case_id=5,
        id=5,
        test_case_key="ANY-T5",
        key="ANY-T5",
        name="test_sth",
        createdOn="",
        project_id=1,
        objective="Test Objective",
        precondition="Test Precondition",
        estimatedTime=123,
        labels=["a_label", "b_label"],
        priority_id=3,
        status_id=new_status_id,
        folder={"id": 100},
        owner={"accountId": "owner100"},
        jira_issues=[],
        urls=[],
        customFields={"custom_field": "custom_value"},
    )


@pytest.mark.parametrize("original_status_id", [1, 2, 3])
def test_zephyr_update_testcase_status_remove(
    pytester, mock_zephyr, mocker, original_status_id
):
    """
    Check that the plugin removes the test case status.
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.folders.FolderEndpoints.get_folders",
        return_value=[
            {
                "id": 100,
                "folderType": "TEST_CASE",
                "name": "test_zephyr_update_testcase_status_remove.py",
                "parentId": None,
            }
        ],
    )
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "objective": "Test objective",
                "precondition": "Test Precondition Original",
                "estimatedTime": 123,
                "labels": ["a_label", "b_label"],
                "priority": {"id": 3, "self": "linkpriority/3"},
                "status": {
                    "id": original_status_id,
                    "self": f"linkstatus/{original_status_id}",
                },
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {"accountId": "owner123", "self": "linkuser/owner123"},
                "customFields": {"custom_field": "custom_value"},
                "links": {"self": "linktestcase/5", "issues": [], "webLinks": []},
            }
        ],
    )
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
"""
    )
    pytester.makepyfile(
        """
                        import pytest

                        @pytest.mark.zephyr_testcase(objective="Test objective",
                                                     precondition="Test Precondition",
                                                     estimatedTime=123,
                                                     ownerId="owner123",
                                                     priorityName="High",
                                                     labels=["a_label", "b_label"],
                                                     customFields={"custom_field": "custom_value"})
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.test_cases.create_test_case.call_count == 0
    mocked_api.test_cases.update_test_case.assert_called_once_with(
        test_case_id=5,
        id=5,
        test_case_key="ANY-T5",
        key="ANY-T5",
        name="test_sth",
        createdOn="",
        project_id=1,
        objective="Test objective",
        precondition="Test Precondition",
        estimatedTime=123,
        labels=["a_label", "b_label"],
        priority_id=3,
        status_id=1,
        folder={"id": 100},
        owner={"accountId": "owner123"},
        jira_issues=[],
        urls=[],
        customFields={"custom_field": "custom_value"},
    )


@pytest.mark.parametrize(
    "new_status_name, new_status_id", [("Obsolete", 3), ("Approved", 2), ("Draft", 1)]
)
def test_zephyr_update_testcase_status_add(
    pytester, mock_zephyr, mocker, new_status_name, new_status_id
):
    """
    Check that the plugin adds the test case status.
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.folders.FolderEndpoints.get_folders",
        return_value=[
            {
                "id": 100,
                "folderType": "TEST_CASE",
                "name": "test_zephyr_update_testcase_status_add.py",
                "parentId": None,
            }
        ],
    )
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "objective": "Test Objective",
                "precondition": "",
                "estimatedTime": 123,
                "labels": ["a_label", "b_label"],
                "priority": {"id": 3, "self": "linkpriority/3"},
                "status": {"id": 1, "self": "linkstatus/1"},
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {},
                "customFields": {"custom_field": "custom_value"},
                "links": {"self": "linktestcase/5", "issues": [], "webLinks": []},
            }
        ],
    )
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
"""
    )
    pytester.makepyfile(
        f"""
                        import pytest

                        @pytest.mark.zephyr_testcase(objective="Test Objective",
                                                     precondition="Test Precondition",
                                                     estimatedTime=123,
                                                     priorityName="High",
                                                     statusName="{new_status_name}",
                                                     ownerId="owner123",
                                                     labels=["a_label", "b_label"],
                                                     customFields={{
                                                         "custom_field": "custom_value"
                                                         }})
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.test_cases.create_test_case.call_count == 0
    mocked_api.test_cases.update_test_case.assert_called_once_with(
        test_case_id=5,
        id=5,
        test_case_key="ANY-T5",
        key="ANY-T5",
        name="test_sth",
        createdOn="",
        project_id=1,
        objective="Test Objective",
        precondition="Test Precondition",
        estimatedTime=123,
        labels=["a_label", "b_label"],
        priority_id=3,
        status_id=new_status_id,
        folder={"id": 100},
        owner={"accountId": "owner123"},
        jira_issues=[],
        urls=[],
        customFields={"custom_field": "custom_value"},
    )


@pytest.mark.parametrize("original_labels", [[], ["a_label"], ["label_0", "label_1"]])
@pytest.mark.parametrize("new_labels", [[], ["a_label", "b_label"], ["label_0"]])
def test_zephyr_update_testcase_labels_change(
    pytester, mock_zephyr, mocker, original_labels, new_labels
):
    """
    Check that the plugin updates the test case labels.
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.folders.FolderEndpoints.get_folders",
        return_value=[
            {
                "id": 100,
                "folderType": "TEST_CASE",
                "name": "test_zephyr_update_testcase_labels_change.py",
                "parentId": None,
            }
        ],
    )
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "objective": "Test objective",
                "precondition": "Test Precondition",
                "estimatedTime": 123,
                "labels": original_labels,
                "priority": {"id": 3, "self": "linkpriority/3"},
                "status": {"id": 3, "self": "linkstatus/3"},
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {"accountId": "owner123", "self": "linkuser/owner123"},
                "customFields": {"custom_field": "custom_value"},
                "links": {"self": "linktestcase/5", "issues": [], "webLinks": []},
            }
        ],
    )
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
"""
    )
    pytester.makepyfile(
        f"""
                        import pytest

                        @pytest.mark.zephyr_testcase(objective="Test Objective",
                                                     precondition="Test Precondition",
                                                     estimatedTime=123,
                                                     priorityName="High",
                                                     statusName="Obsolete",
                                                     ownerId="owner100",
                                                     labels={new_labels},
                                                     customFields={{
                                                         "custom_field": "custom_value"
                                                         }})
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.test_cases.create_test_case.call_count == 0
    mocked_api.test_cases.update_test_case.assert_called_once_with(
        test_case_id=5,
        id=5,
        test_case_key="ANY-T5",
        key="ANY-T5",
        name="test_sth",
        createdOn="",
        project_id=1,
        objective="Test Objective",
        precondition="Test Precondition",
        estimatedTime=123,
        labels=new_labels,
        priority_id=3,
        status_id=3,
        folder={"id": 100},
        owner={"accountId": "owner100"},
        jira_issues=[],
        urls=[],
        customFields={"custom_field": "custom_value"},
    )
