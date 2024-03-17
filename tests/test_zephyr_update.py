# -*- coding: utf-8 -*-
def test_zephyr_update_change_objective(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugins updates the objective of the test case
    """
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
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugins creates the objective if it did not exist previously
    """
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


def test_zephyr_update_remove_objective(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugins removes the objective
    """
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


def test_zephyr_update_change_precondition(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugins updates the precondition of the test case
    """
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


def test_zephyr_update_add_precondition(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugins creates the precondition if it did not exist previously
    """
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


def test_zephyr_update_change_estimatedTime(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin updates the estimatedTime of the test case
    """
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


def test_zephyr_update_add_estimatedTime(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin adds the estimatedTime of the test case
    """
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


def test_zephyr_update_remove_estimatedTime(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin adds the estimatedTime of the test case
    """
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


def test_zephyr_update_change_priorityName(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin updates the priorityName of the test case
    """
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


def test_zephyr_update_add_priorityName(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin adds the priorityName of the test case
    """
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


def test_zephyr_update_remove_priorityName(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin adds the priorityName of the test case
    """
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


def test_zephyr_update_change_statusName(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin updates the statusName of the test case
    """
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


def test_zephyr_update_add_statusName(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin adds the statusName of the test case
    """
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


def test_zephyr_update_remove_statusName(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin adds the statusName of the test case
    """
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


def test_zephyr_update_change_ownerId(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin updates the ownerId of the test case
    """
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


def test_zephyr_update_add_ownerId(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin adds the ownerId of the test case
    """
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


def test_zephyr_update_remove_ownerId(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin adds the ownerId of the test case
    """
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


def test_zephyr_update_change_labels_one_common(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin updates the labels of the test case
    """
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


def test_zephyr_update_change_labels_all(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin updates the labels of the test case
    """
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


def test_zephyr_update_add_labels_empty(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin adds the labels of the test case
    """
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


def test_zephyr_update_add_labels_others(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin adds the labels of the test case
    """
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


def test_zephyr_update_remove_labels_some(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin adds the labels of the test case
    """
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


def test_zephyr_update_remove_labels_all(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin adds the labels of the test case
    """
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


def test_zephyr_update_change_jira_issues_one_common(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin updates the jira_issues of the test case
    """
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
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", jira_issues=[\"TP-17\", \"TP-7\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\",jira_issues=[\"TP-17\", \"TP-8\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_change_jira_issues_all(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin updates the jira_issues of the test case
    """
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
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", jira_issues=[\"TP-17\", \"TP-7\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", jira_issues=[\"TP-13\", \"TP-6\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_add_jira_issues_empty(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin adds the jira_issues of the test case
    """
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
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", jira_issues=[\"TP-17\", \"TP-7\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_add_jira_issues_others(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin adds the jira_issues of the test case
    """
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
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", jira_issues=[\"TP-17\", \"TP-7\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", jira_issues=[\"TP-17\", \"TP-7\", \"TP-8\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_remove_jira_issues_some(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin adds the jira_issues of the test case
    """
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
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", jira_issues=[\"TP-17\", \"TP-7\", \"TP-8\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", jira_issues=[\"TP-17\", \"TP-8\"])
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_update_remove_jira_issues_all(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin adds the jira_issues of the test case
    """
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
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\", jira_issues=[\"TP-17\", \"TP-8\"])
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


def test_zephyr_update_change_urls_one_common(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin updates the urls of the test case
    """
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
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin updates the urls of the test case
    """
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


def test_zephyr_update_add_urls_empty(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin adds the urls of the test case
    """
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


def test_zephyr_update_add_urls_others(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin adds the urls of the test case
    """
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


def test_zephyr_update_remove_urls_some(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin adds the urls of the test case
    """
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


def test_zephyr_update_remove_urls_all(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that the plugin adds the urls of the test case
    """
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
