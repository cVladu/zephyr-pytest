# -*- coding: utf-8 -*-
def test_zephyr_create_testcase_default(pytester, mock_zephyr):
    """
    Check that the plugin creates a test case with default values.
    """
    mocked_api = mock_zephyr
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

                        @pytest.mark.zephyr_testcase
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_case.assert_called_with(
        "ANY",
        "test_sth",
        folderId=100,
        priority_id=2,
        status_id=1,
        jira_issues=[],
        urls=[],
    )
    assert mocked_api.test_cases.create_test_case.call_count == 1


def test_zephyr_create_testcase_objective(pytester, mock_zephyr):
    """
    Check that the plugin creates a test case with objective.
    """
    mocked_api = mock_zephyr
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

                        @pytest.mark.zephyr_testcase(objective="Test objective")
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_case.assert_called_with(
        "ANY",
        "test_sth",
        folderId=100,
        priority_id=2,
        status_id=1,
        objective="Test objective",
        jira_issues=[],
        urls=[],
    )
    assert mocked_api.test_cases.create_test_case.call_count == 1


def test_zephyr_create_testcase_precondition(pytester, mock_zephyr):
    """
    Check that the plugin creates a test case with precondition.
    """
    mocked_api = mock_zephyr
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

                        @pytest.mark.zephyr_testcase(precondition="Test precondition")
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_case.assert_called_with(
        "ANY",
        "test_sth",
        folderId=100,
        priority_id=2,
        status_id=1,
        precondition="Test precondition",
        jira_issues=[],
        urls=[],
    )
    assert mocked_api.test_cases.create_test_case.call_count == 1


def test_zephyr_create_testcase_estimatedTime(pytester, mock_zephyr):
    """
    Check that the plugin creates a test case with estimatedTime.
    """
    mocked_api = mock_zephyr
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

                        @pytest.mark.zephyr_testcase(estimatedTime=123123)
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_case.assert_called_with(
        "ANY",
        "test_sth",
        folderId=100,
        priority_id=2,
        status_id=1,
        estimatedTime=123123,
        jira_issues=[],
        urls=[],
    )
    assert mocked_api.test_cases.create_test_case.call_count == 1


def test_zephyr_create_testcase_priorityName_high(pytester, mock_zephyr):
    """
    Check that the plugin creates a test case with priority high.
    """
    mocked_api = mock_zephyr
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

                        @pytest.mark.zephyr_testcase(priorityName="High")
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_case.assert_called_with(
        "ANY",
        "test_sth",
        folderId=100,
        priorityName="High",
        priority_id=3,
        status_id=1,
        jira_issues=[],
        urls=[],
    )
    assert mocked_api.test_cases.create_test_case.call_count == 1


def test_zephyr_create_testcase_priorityName_medium(pytester, mock_zephyr):
    """
    Check that the plugin creates a test case with priority medium.
    """
    mocked_api = mock_zephyr
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

                        @pytest.mark.zephyr_testcase(priorityName="Medium")
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_case.assert_called_with(
        "ANY",
        "test_sth",
        folderId=100,
        priorityName="Medium",
        priority_id=2,
        status_id=1,
        jira_issues=[],
        urls=[],
    )
    assert mocked_api.test_cases.create_test_case.call_count == 1


def test_zephyr_create_testcase_priorityName_low(pytester, mock_zephyr):
    """
    Check that the plugin creates a test case with priority low.
    """
    mocked_api = mock_zephyr
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

                        @pytest.mark.zephyr_testcase(priorityName="Low")
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_case.assert_called_with(
        "ANY",
        "test_sth",
        folderId=100,
        priorityName="Low",
        priority_id=1,
        status_id=1,
        jira_issues=[],
        urls=[],
    )
    assert mocked_api.test_cases.create_test_case.call_count == 1


def test_zephyr_create_testcase_statusName_draft(pytester, mock_zephyr):
    """
    Check that the plugin creates a test case with status draft.
    """
    mocked_api = mock_zephyr
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

                        @pytest.mark.zephyr_testcase(statusName="Draft")
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_case.assert_called_with(
        "ANY",
        "test_sth",
        folderId=100,
        statusName="Draft",
        priority_id=2,
        status_id=1,
        jira_issues=[],
        urls=[],
    )
    assert mocked_api.test_cases.create_test_case.call_count == 1


def test_zephyr_create_testcase_statusName_approved(pytester, mock_zephyr):
    """
    Check that the plugin creates a test case with status approved.
    """
    mocked_api = mock_zephyr
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

                        @pytest.mark.zephyr_testcase(statusName="Approved")
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_case.assert_called_with(
        "ANY",
        "test_sth",
        folderId=100,
        statusName="Approved",
        priority_id=2,
        status_id=2,
        jira_issues=[],
        urls=[],
    )
    assert mocked_api.test_cases.create_test_case.call_count == 1


def test_zephyr_create_testcase_statusName_obsolete(pytester, mock_zephyr):
    """
    Check that the plugin creates a test case with status obsolete.
    """
    mocked_api = mock_zephyr
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

                        @pytest.mark.zephyr_testcase(statusName="Obsolete")
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_case.assert_called_with(
        "ANY",
        "test_sth",
        folderId=100,
        statusName="Obsolete",
        priority_id=2,
        status_id=3,
        jira_issues=[],
        urls=[],
    )
    assert mocked_api.test_cases.create_test_case.call_count == 1


def test_zephyr_create_testcase_statusName_ownerId(pytester, mock_zephyr):
    """
    Check that the plugin creates a test case with ownerId set.
    """
    mocked_api = mock_zephyr
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

                        @pytest.mark.zephyr_testcase(ownerId="abc123cde")
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_case.assert_called_with(
        "ANY",
        "test_sth",
        folderId=100,
        priority_id=2,
        status_id=1,
        ownerId="abc123cde",
        jira_issues=[],
        urls=[],
    )
    assert mocked_api.test_cases.create_test_case.call_count == 1


def test_zephyr_create_testcase_labels_only_one(pytester, mock_zephyr):
    """
    Check that the plugin creates a test case with one label set.
    """
    mocked_api = mock_zephyr
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

                        @pytest.mark.zephyr_testcase(labels=["a_label"])
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_case.assert_called_with(
        "ANY",
        "test_sth",
        folderId=100,
        priority_id=2,
        status_id=1,
        labels=["a_label"],
        jira_issues=[],
        urls=[],
    )
    assert mocked_api.test_cases.create_test_case.call_count == 1


def test_zephyr_create_testcase_labels_multiple(pytester, mock_zephyr):
    """
    Check that the plugin creates a test case with multiple labels set.
    """
    mocked_api = mock_zephyr
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

                        @pytest.mark.zephyr_testcase(labels=["a_label", "b_label"])
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_case.assert_called_with(
        "ANY",
        "test_sth",
        folderId=100,
        priority_id=2,
        status_id=1,
        labels=["a_label", "b_label"],
        jira_issues=[],
        urls=[],
    )
    assert mocked_api.test_cases.create_test_case.call_count == 1


def test_zephyr_create_testcase_customFields(pytester, mock_zephyr):
    """
    Check that the plugin creates a test case with custom fields set.
    """
    mocked_api = mock_zephyr
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

                        @pytest.mark.zephyr_testcase(customFields={"custom_field": "custom_value"})
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_case.assert_called_with(
        "ANY",
        "test_sth",
        folderId=100,
        priority_id=2,
        status_id=1,
        customFields={"custom_field": "custom_value"},
        jira_issues=[],
        urls=[],
    )
    assert mocked_api.test_cases.create_test_case.call_count == 1


def test_zephyr_create_testcase_all_fileds(pytester, mock_zephyr):
    """
    Check that the plugin creates a test case with all fields set.
    """
    mocked_api = mock_zephyr
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
    mocked_api.test_cases.create_test_case.assert_called_with(
        "ANY",
        "test_sth",
        folderId=100,
        priorityName="High",
        priority_id=3,
        statusName="Obsolete",
        status_id=3,
        objective="Test Objective",
        precondition="Test Precondition",
        estimatedTime=123,
        ownerId="owner123",
        labels=["a_label", "b_label"],
        customFields={"custom_field": "custom_value"},
        jira_issues=[],
        urls=[],
    )
    assert mocked_api.test_cases.create_test_case.call_count == 1
