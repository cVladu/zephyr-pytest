# -*- coding: utf-8 -*-


def test_zephyr_report_passed(pytester, config_tokens):
    """
    Check that zephyr correctly reports passed test case
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


def test_zephyr_report_failed(pytester, config_tokens):
    """
    Check that zephyr correctly reports failed test case
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
    pytester,
    config_tokens,
):
    """
    Check that zephyr correctly reports failed test case
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


def test_zephyr_report_skipped_reason(pytester, config_tokens):
    """
    Check that zephyr correctly reports skipped test case
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


def test_zephyr_report_skipped_if(pytester, config_tokens):
    """
    Check that zephyr correctly reports skipped with a reason test case
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


def test_zephyr_report_xfail(pytester, config_tokens):
    """
    Check that zephyr correctly reports xfailed test case
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


def test_zephyr_report_xfail_if_reason(pytester, config_tokens):
    """
    Check that zephyr correctly reports xfailed with a reason test case
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


def test_zephyr_report_xpass(pytester, config_tokens):
    """
    Check that zephyr correctly reports xpassed test case
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


def test_zephyr_report_xpass_if_reason(pytester, config_tokens):
    """
    Check that zephyr correctly reports xpassed test case
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


def test_zephyr_report_estimated_time(pytester, config_tokens):
    """
    Check that zephyr correctly reports estimated time for a test case
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
zephyr_testcycle_name = Test Cycle Estimated Time
"""
    )
    pytester.makepyfile(
        """
import pytest
from time import sleep
from random import randint
@pytest.mark.zephyr_testcase()
def test_sth():
    sleep(randint(1, 20))
    assert 1 + 2 == 3
"""
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0


def test_zephyr_report_custom_mapping(pytester, config_tokens):
    """
    Check that zephyr correctly reports given the new mapping
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
zephyr_testcycle_name = Test Cycle Custom Mapping
"""
    )
    pytester.makepyfile(
        """
import pytest
@pytest.mark.zephyr_testcase()
def test_custom_pass():
    assert 1 + 2 == 3

@pytest.mark.zephyr_testcase()
def test_custom_fail():
    sleep(randint(1, 20))
    assert 1 + 2 == 3

@pytest.mark.zephyr_testcase()
@pytest.mark.skip
def test_custom_skip():
    assert 1 + 2 == 3

@pytest.mark.zephyr_testcase()
@pytest.mark.xfail
def test_custom_xfail():
    assert 1 + 2 == 5

@pytest.mark.zephyr_testcase()
@pytest.mark.xfail
def test_custom_xpass():
    assert 1 + 2 == 3
"""
    )
    pytester.makeconftest(
        """
import pytest_zephyr

pytest_zephyr.register_report_mapping(
    {
        "passed": "CUSTOM_PASS",
        "failed": "CUSTOM_FAIL",
        "skipped": "CUSTOM_SKIP",
        "xfailed": "CUSTOM_XFAIL",
        "xpassed": "CUSTOM_XPASS"
    }
)
    """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret != 0
