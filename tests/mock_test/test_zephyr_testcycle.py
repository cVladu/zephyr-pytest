# -*- coding: utf-8 -*-
import pytest
from packaging.version import Version


@pytest.mark.skipif(
    Version(pytest.__version__) < Version("8.0.0"),
    reason="This test fails for pytest version 7.4.0 and below and I do not know why",
)
def test_zephyr_create_test_cycle_default(pytester, mock_zephyr):
    """
    Check that the plugin creates the test cycle with default parameters
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
    mocked_api.executions.create_test_cycle.assert_called_once_with(
        project_key="ANY", name="Pytest run", description="", ownerId=None
    )


@pytest.mark.skipif(
    Version(pytest.__version__) < Version("8.0.0"),
    reason="This test fails for pytest version 7.4.0 and below and I do not know why",
)
def test_zephyr_create_test_cycle_no_publish(pytester, mock_zephyr):
    """
    Check that the plugin does NOT create the test cycle when given the no publish option is given
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
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    assert mocked_api.executions.create_test_cycle.call_count == 0


@pytest.mark.skipif(
    Version(pytest.__version__) < Version("8.0.0"),
    reason="This test fails for pytest version 7.4.0 and below and I do not know why",
)
def test_zephyr_create_test_cycle_given_name(pytester, mock_zephyr):
    """
    Check that the plugin creates the test cycle with given name
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
zephyr_testcycle_name = Given Name
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
    mocked_api.executions.create_test_cycle.assert_called_once_with(
        project_key="ANY", name="Given Name", description="", ownerId=None
    )


@pytest.mark.skipif(
    Version(pytest.__version__) < Version("8.0.0"),
    reason="This test fails for pytest version 7.4.0 and below and I do not know why",
)
def test_zephyr_create_test_cycle_given_description(pytester, mock_zephyr):
    """
    Check that the plugin creates the test cycle with given description
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
zephyr_testcycle_description = Given Description
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
    mocked_api.executions.create_test_cycle.assert_called_once_with(
        project_key="ANY",
        name="Pytest run",
        description="Given Description",
        ownerId=None,
    )


@pytest.mark.skipif(
    Version(pytest.__version__) < Version("8.0.0"),
    reason="This test fails for pytest version 7.4.0 and below and I do not know why",
)
def test_zephyr_create_test_cycle_given_name_and_description(pytester, mock_zephyr):
    """
    Check that the plugin creates the test cycle with given name and description
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
zephyr_testcycle_name = Given Name 2
zephyr_testcycle_description = Given Description 2
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
    mocked_api.executions.create_test_cycle.assert_called_once_with(
        project_key="ANY",
        name="Given Name 2",
        description="Given Description 2",
        ownerId=None,
    )


@pytest.mark.skipif(
    Version(pytest.__version__) < Version("8.0.0"),
    reason="This test fails for pytest version 7.4.0 and below and I do not know why",
)
def test_zephyr_create_test_cycle_owner_id(pytester, mock_zephyr):
    """
    Check that the plugin creates the test cycle with given owner id
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
    result = pytester.runpytest("--zephyr", "--zephyr-owner-id=given_owner_id")
    assert result.ret == 0
    mocked_api.executions.create_test_cycle.assert_called_once_with(
        project_key="ANY", name="Pytest run", description="", ownerId="given_owner_id"
    )


@pytest.mark.skipif(
    Version(pytest.__version__) < Version("8.0.0"),
    reason="This test fails for pytest version 7.4.0 and below and I do not know why",
)
def test_zephyr_create_test_cycle_given_name_os_environ(
    pytester, mock_zephyr, monkeypatch
):
    """
    Check that the plugin creates the test cycle with given name through os environ
    with higher priority
    """
    mocked_api = mock_zephyr
    monkeypatch.setenv("ZEPHYR_TESTCYCLE_NAME", "Environ Name")
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
zephyr_testcycle_name = Config Name
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
    mocked_api.executions.create_test_cycle.assert_called_once_with(
        project_key="ANY", name="Environ Name", description="", ownerId=None
    )


@pytest.mark.skipif(
    Version(pytest.__version__) < Version("8.0.0"),
    reason="This test fails for pytest version 7.4.0 and below and I do not know why",
)
def test_zephyr_create_test_cycle_given_description_os_environ(
    pytester, mock_zephyr, monkeypatch
):
    """
    Check that the plugin creates the test cycle with given description through os environ
    with higher priority
    """
    mocked_api = mock_zephyr
    monkeypatch.setenv("ZEPHYR_TESTCYCLE_DESCRIPTION", "Environ Description")
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
zephyr_testcycle_description = Given Description
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
    mocked_api.executions.create_test_cycle.assert_called_once_with(
        project_key="ANY",
        name="Pytest run",
        description="Environ Description",
        ownerId=None,
    )


@pytest.mark.skipif(
    Version(pytest.__version__) < Version("8.0.0"),
    reason="This test fails for pytest version 7.4.0 and below and I do not know why",
)
def test_zephyr_create_test_cycle_given_name_and_description_os_environ(
    pytester, mock_zephyr, monkeypatch
):
    """
    Check that the plugin creates the test cycle with given name and description
    through os environ with higher priority
    """
    mocked_api = mock_zephyr
    monkeypatch.setenv("ZEPHYR_TESTCYCLE_NAME", "Environ Name 1")
    monkeypatch.setenv("ZEPHYR_TESTCYCLE_DESCRIPTION", "Environ Description 1")
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
zephyr_testcycle_name = Given Name 2
zephyr_testcycle_description = Given Description 2
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
    mocked_api.executions.create_test_cycle.assert_called_once_with(
        project_key="ANY",
        name="Environ Name 1",
        description="Environ Description 1",
        ownerId=None,
    )


@pytest.mark.skipif(
    Version(pytest.__version__) < Version("8.0.0"),
    reason="This test fails for pytest version 7.4.0 and below and I do not know why",
)
def test_zephyr_create_test_cycle_owner_id_os_environ(
    pytester, mock_zephyr, monkeypatch
):
    """
    Check that the plugin creates the test cycle with given owner id through os environ
    """
    mocked_api = mock_zephyr
    monkeypatch.setenv("ZEPHYR_OWNER_ID", "owner-os-environ")
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
    mocked_api.executions.create_test_cycle.assert_called_once_with(
        project_key="ANY", name="Pytest run", description="", ownerId="owner-os-environ"
    )


@pytest.mark.skipif(
    Version(pytest.__version__) < Version("8.0.0"),
    reason="This test fails for pytest version 7.4.0 and below and I do not know why",
)
def test_zephyr_create_test_cycle_owner_id_os_environ_and_option(
    pytester, mock_zephyr, monkeypatch
):
    """
    Check that the plugin creates the test cycle with given owner id
    through os environ and pytest option (higher priority)
    """
    mocked_api = mock_zephyr
    monkeypatch.setenv("ZEPHYR_OWNER_ID", "owner-os-environ")
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
    result = pytester.runpytest("--zephyr", "--zephyr-owner-id=owner-option")
    assert result.ret == 0
    mocked_api.executions.create_test_cycle.assert_called_once_with(
        project_key="ANY", name="Pytest run", description="", ownerId="owner-option"
    )
