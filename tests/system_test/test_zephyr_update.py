# -*- coding: utf-8 -*-


def test_zephyr_update_change_objective(pytester, config_tokens):
    """
    Check that the plugins updates the objective of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case updated\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_add_objective(
    pytester,
    config_tokens,
):
    """
    Check that the plugins creates the objective if it did not exist previously
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case added\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_remove_objective(pytester, config_tokens):
    """
    Check that the plugins removes the objective
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case removed\",precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_change_precondition(pytester, config_tokens):
    """
    Check that the plugins updates the precondition of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case updated\", precondition="A precondition updated", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_add_precondition(pytester, config_tokens):
    """
    Check that the plugins creates the precondition if it did not exist previously
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition added", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_change_estimatedTime(pytester, config_tokens):
    """
    Check that the plugin updates the estimatedTime of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=1800000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_add_estimatedTime(pytester, config_tokens):
    """
    Check that the plugin adds the estimatedTime of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=36000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_remove_estimatedTime(pytester, config_tokens):
    """
    Check that the plugin adds the estimatedTime of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_change_priorityName(pytester, config_tokens):
    """
    Check that the plugin updates the priorityName of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"Low\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_add_priorityName(pytester, config_tokens):
    """
    Check that the plugin adds the priorityName of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"Low\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_remove_priorityName(pytester, config_tokens):
    """
    Check that the plugin adds the priorityName of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_change_statusName(pytester, config_tokens):
    """
    Check that the plugin updates the statusName of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Deprecated\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_add_statusName(pytester, config_tokens):
    """
    Check that the plugin adds the statusName of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Deprecated\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_remove_statusName(pytester, config_tokens):
    """
    Check that the plugin adds the statusName of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_change_ownerId(pytester, config_tokens):
    """
    Check that the plugin updates the ownerId of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"712020:eff88cc9-b099-4817-92b5-3bf1691bfc2f\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_add_ownerId(pytester, config_tokens):
    """
    Check that the plugin adds the ownerId of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_remove_ownerId(pytester, config_tokens):
    """
    Check that the plugin adds the ownerId of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_change_labels_one_common(pytester, config_tokens):
    """
    Check that the plugin updates the labels of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_3\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_change_labels_all(pytester, config_tokens):
    """
    Check that the plugin updates the labels of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_4\", \"label_3\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_add_labels_empty(pytester, config_tokens):
    """
    Check that the plugin adds the labels of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_add_labels_others(pytester, config_tokens):
    """
    Check that the plugin adds the labels of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\", \"label_3\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_remove_labels_some(pytester, config_tokens):
    """
    Check that the plugin adds the labels of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_remove_labels_all(pytester, config_tokens):
    """
    Check that the plugin adds the labels of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_change_jira_issues_one_common(pytester, config_tokens):
    """
    Check that the plugin updates the jira_issues of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        f"""  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", jira_issues=[\"{project_key}-17\", \"{project_key}-7\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        f"""  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\",jira_issues=[\"{project_key}-17\", \"{project_key}-8\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_change_jira_issues_all(pytester, config_tokens):
    """
    Check that the plugin updates the jira_issues of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        f"""  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", jira_issues=[\"{project_key}-17\", \"{project_key}-7\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        f"""  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", jira_issues=[\"{project_key}-13\", \"{project_key}-6\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_add_jira_issues_empty(pytester, config_tokens):
    """
    Check that the plugin adds the jira_issues of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        f"""  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", jira_issues=[\"{project_key}-17\", \"{project_key}-7\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_add_jira_issues_others(pytester, config_tokens):
    """
    Check that the plugin adds the jira_issues of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        f"""  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", jira_issues=[\"{project_key}-17\", \"{project_key}-7\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        f"""  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", jira_issues=[\"{project_key}-17\", \"{project_key}-7\", \"{project_key}-8\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_remove_jira_issues_some(pytester, config_tokens):
    """
    Check that the plugin adds the jira_issues of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        f"""  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", jira_issues=[\"{project_key}-17\", \"{project_key}-7\", \"{project_key}-8\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        f"""  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", jira_issues=[\"{project_key}-17\", \"{project_key}-8\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_remove_jira_issues_all(pytester, config_tokens):
    """
    Check that the plugin adds the jira_issues of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", jira_issues=[\"{project_key}-17\", \"{project_key}-8\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_change_urls_one_common(pytester, config_tokens):
    """
    Check that the plugin updates the urls of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", urls=[\"google.com\", \"example.com\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", urls=[\"google.com\", \"facebook.com\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_change_urls_all(
    pytester,
    config_tokens,
):
    """
    Check that the plugin updates the urls of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", urls=[\"google.com\", \"facebook.com\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", urls=[\"example.com\", \"twitter.com\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_add_urls_empty(pytester, config_tokens):
    """
    Check that the plugin adds the urls of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", urls=[\"example.com\", \"twitter.com\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_add_urls_others(pytester, config_tokens):
    """
    Check that the plugin adds the urls of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", urls=[\"example.com\", \"twitter.com\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", urls=[\"example.com\", \"twitter.com\", \"facebook.com\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_remove_urls_some(pytester, config_tokens):
    """
    Check that the plugin adds the urls of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", urls=[\"example.com\", \"twitter.com\", \"facebook.com\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", urls=[\"facebook.com\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_remove_urls_all(pytester, config_tokens):
    """
    Check that the plugin adds the urls of the test case
    """
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
[pytest]
zephyr_project_key = {project_key}
zephyr_auth_token = {auth_token}
zephyr_jira_base_url = {jira_base_url}
zephyr_jira_email = {jira_email}
zephyr_jira_token = {jira_token}
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", urls=[\"example.com\", \"twitter.com\", \"facebook.com\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
