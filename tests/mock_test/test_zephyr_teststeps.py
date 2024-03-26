# -*- coding: utf-8 -*-
from pytest_zephyr._zephyr_interface import TEST_STEPS_OVERWRITE


def test_zephyr_create_teststeps_default_no_docstring(pytester, mock_zephyr, mocker):
    """
    Check that the plugin still tries to create the test steps even if there is no docstring
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.create_test_case",
        return_value={"id": 200, "key": "ANY-T200"},
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

                        @pytest.mark.zephyr_testcase
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_script.assert_called_once_with(
        "ANY-T200", script_type="plain", text=" "
    )
    assert mocked_api.test_cases.create_test_steps.call_count == 0


def test_zephyr_create_teststeps_default_docstring(pytester, mock_zephyr, mocker):
    """
    Check that the plugin creates the test steps from the docstring
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.create_test_case",
        return_value={"id": 200, "key": "ANY-T200"},
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

                        @pytest.mark.zephyr_testcase
                        def test_sth():
                            \"\"\"Test steps in the docstring\"\"\"
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_script.assert_called_once_with(
        "ANY-T200", script_type="plain", text="Test steps in the docstring"
    )
    assert mocked_api.test_cases.create_test_steps.call_count == 0


def test_zephyr_create_teststeps_default_docstring_new_line(
    pytester, mock_zephyr, mocker
):
    """
    Check that the plugin creates the test steps from the docstring
    and replaces the new lines
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.create_test_case",
        return_value={"id": 200, "key": "ANY-T200"},
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

                        @pytest.mark.zephyr_testcase
                        def test_sth():
                            \"\"\"First line
                            Second line
                            Third line
                            \"\"\"
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_script.assert_called_once_with(
        "ANY-T200",
        script_type="plain",
        text="First line<br>    Second line<br>    Third line<br>    ",
    )
    assert mocked_api.test_cases.create_test_steps.call_count == 0


def test_zephyr_create_teststeps_specified_no_docstring(pytester, mock_zephyr, mocker):
    """
    Check that the plugin still tries to create the test steps even if there is no docstring
    with given kwarg value
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.create_test_case",
        return_value={"id": 200, "key": "ANY-T200"},
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

                        @pytest.mark.zephyr_testcase(test_steps="doc")
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_script.assert_called_once_with(
        "ANY-T200", script_type="plain", text=" "
    )
    assert mocked_api.test_cases.create_test_steps.call_count == 0


def test_zephyr_create_teststeps_specified_docstring(pytester, mock_zephyr, mocker):
    """
    Check that the plugin creates the test steps from the docstring
    with given kwarg value
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.create_test_case",
        return_value={"id": 200, "key": "ANY-T200"},
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

                        @pytest.mark.zephyr_testcase(test_steps="doc")
                        def test_sth():
                            \"\"\"Test steps in the docstring\"\"\"
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_script.assert_called_once_with(
        "ANY-T200", script_type="plain", text="Test steps in the docstring"
    )
    assert mocked_api.test_cases.create_test_steps.call_count == 0


def test_zephyr_create_teststeps_specified_docstring_new_line(
    pytester, mock_zephyr, mocker
):
    """
    Check that the plugin creates the test steps from the docstring
    and replaces the new lines with given kwarg value
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.create_test_case",
        return_value={"id": 200, "key": "ANY-T200"},
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

                        @pytest.mark.zephyr_testcase(test_steps="doc")
                        def test_sth():
                            \"\"\"First line
                            Second line
                            Third line
                            \"\"\"
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_script.assert_called_once_with(
        "ANY-T200",
        script_type="plain",
        text="First line<br>    Second line<br>    Third line<br>    ",
    )
    assert mocked_api.test_cases.create_test_steps.call_count == 0


def test_zephyr_create_teststeps_given(pytester, mock_zephyr, mocker):
    """
    Check that the plugin creates the test steps from the given string
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.create_test_case",
        return_value={"id": 200, "key": "ANY-T200"},
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

                        @pytest.mark.zephyr_testcase(test_steps="Given steps through kwarg")  # noqa: E501
                        def test_sth():
                            \"\"\"
                            This shall be ignored
                            \"\"\"
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_script.assert_called_once_with(
        "ANY-T200",
        script_type="plain",
        text="Given steps through kwarg",
    )
    assert mocked_api.test_cases.create_test_steps.call_count == 0


def test_zephyr_create_teststeps_given_new_line(pytester, mock_zephyr, mocker):
    """
    Check that the plugin creates the test steps from the docstring
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.create_test_case",
        return_value={"id": 200, "key": "ANY-T200"},
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

                        @pytest.mark.zephyr_testcase(test_steps="First line\\nSecond line\\nThird line")  # noqa: E501
                        def test_sth():
                            \"\"\"
                            This shall be ignored
                            \"\"\"
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_script.assert_called_once_with(
        "ANY-T200",
        script_type="plain",
        text="First line<br>Second line<br>Third line",
    )
    assert mocked_api.test_cases.create_test_steps.call_count == 0


def test_zephyr_create_teststeps_given_test_steps(pytester, mock_zephyr, mocker):
    """
    Check that the plugin creates the test steps from list of steps
    """
    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.create_test_case",
        return_value={"id": 200, "key": "ANY-T200"},
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

                        @pytest.mark.zephyr_testcase(test_steps=[
                            {"step": "First step", "expected": "Expected for first step"},
                            {"step": "Second step, without expectation"}])
                        def test_sth():
                            \"\"\"
                            This shall be ignored
                            \"\"\"
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.test_cases.create_test_steps.assert_called_once_with(
        "ANY-T200",
        mode=TEST_STEPS_OVERWRITE,
        items=[
            {
                "inline": {
                    "description": "First step",
                    "testData": "",
                    "expectedResult": "Expected for first step",
                }
            },
            {
                "inline": {
                    "description": "Second step, without expectation",
                    "testData": "",
                    "expectedResult": "",
                }
            },
        ],
    )
    assert mocked_api.test_cases.create_test_script.call_count == 0
