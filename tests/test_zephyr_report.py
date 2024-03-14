# -*- coding: utf-8 -*-
def test_zephyr_report_passed(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that zephyr correctly reports passed test case
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
zephyr_testcycle_name = Test Cycle Passed
"""
    )
    pytester.makepyfile(
        """
import pytest
@pytest.mark.zephyr_testcase()
def test_sth():
    assert 1 + 2 == 3
"""
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0


def test_zephyr_report_failed(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that zephyr correctly reports failed test case
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
zephyr_testcycle_name = Test Cycle Failed
"""
    )
    pytester.makepyfile(
        """
import pytest
@pytest.mark.zephyr_testcase()
def test_sth():
    assert 1 + 2 == 5
"""
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret != 0


def test_zephyr_report_skipped(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that zephyr correctly reports failed test case
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
zephyr_testcycle_name = Test Cycle Skipped
"""
    )
    pytester.makepyfile(
        """
import pytest
@pytest.mark.zephyr_testcase()
@pytest.mark.skip
def test_sth():
    assert 1 + 2 == 5

@pytest.mark.zephyr_testcase()
def test_sth_else():
    assert 1 + 2 == 3
"""
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0


def test_zephyr_report_skipped_reason(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that zephyr correctly reports skipped test case
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
zephyr_testcycle_name = Test Cycle Skipped Reason
"""
    )
    pytester.makepyfile(
        """
import pytest
@pytest.mark.zephyr_testcase()
@pytest.mark.skip(reason="I don't want to run this for some reason")
def test_sth():
    assert 1 + 2 == 5
"""
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0


def test_zephyr_report_skipped_if(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that zephyr correctly reports skipped with a reason test case
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
zephyr_testcycle_name = Test Cycle Skipped If Reason
"""
    )
    pytester.makepyfile(
        """
import pytest
@pytest.mark.zephyr_testcase()
@pytest.mark.skipif(1+1 == 2, reason="I don't want to run this test")
def test_sth():
    assert 1 + 2 == 5
"""
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0


def test_zephyr_report_xfail(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that zephyr correctly reports xfailed test case
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
zephyr_testcycle_name = Test Cycle Xfail
"""
    )
    pytester.makepyfile(
        """
import pytest
@pytest.mark.zephyr_testcase()
@pytest.mark.xfail
def test_sth():
    assert 1 + 2 == 5
"""
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0


def test_zephyr_report_xfail_if_reason(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that zephyr correctly reports xfailed with a reason test case
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
zephyr_testcycle_name = Test Cycle Xfailed If Reason
"""
    )
    pytester.makepyfile(
        """
import pytest
@pytest.mark.zephyr_testcase()
@pytest.mark.xfail(1+1 == 2, reason="I don't want to pass this testcase")
def test_sth():
    assert 1 + 2 == 5
"""
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0


def test_zephyr_report_xpass(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that zephyr correctly reports xpassed test case
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
zephyr_testcycle_name = Test Cycle Xpass
"""
    )
    pytester.makepyfile(
        """
import pytest
@pytest.mark.zephyr_testcase()
@pytest.mark.xfail
def test_sth():
    assert 1 + 2 == 3
"""
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0


def test_zephyr_report_xpass_if_reason(
    pytester, project_key, auth_token, jira_base_url, jira_email, jira_token
):
    """
    Check that zephyr correctly reports xpassed test case
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
zephyr_testcycle_name = Test Cycle Xpass If Reason
"""
    )
    pytester.makepyfile(
        """
import pytest
@pytest.mark.zephyr_testcase()
@pytest.mark.xfail(1+1 == 2, reason="I don't want to pass this testcase")
def test_sth():
    assert 1 + 2 == 3
"""
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
