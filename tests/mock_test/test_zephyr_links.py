# -*- coding: utf-8 -*-
import pytest


def test_zephyr_create_links_jira_issues(pytester, mock_zephyr, mock_jira, mocker):
    """
    Check that the plugin creates the links to jira issues from the test case.
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

                        @pytest.mark.zephyr_testcase(jira_issues=["JIRA-1234"])
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.links.create_issue_link.assert_called_with("ANY-T200", 1234)


@pytest.mark.parametrize(
    "issue_to_keep, link_to_delete", [("JIRA-1234", 5432), ("JIRA-2345", 4321)]
)
def test_zephyr_deletes_links_jira_issues(
    pytester, mock_zephyr, mock_jira, mocker, issue_to_keep, link_to_delete
):
    """
    Check that the plugin deletes the links to jira issue from the test case.
    """

    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "priority": {"id": 2, "self": "linkpriority/2"},
                "status": {"id": 1, "self": "linkstatus/1"},
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {"accountId": "owner123", "self": "linkuser/owner123"},
                "links": {
                    "self": "linktestcase/5",
                    "issues": [
                        {"issueId": 1234, "id": 4321},
                        {"issueId": 2345, "id": 5432},
                    ],
                    "webLinks": [],
                },
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

                        @pytest.mark.zephyr_testcase(jira_issues=["{issue_to_keep}"])
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.links.create_issue_link.call_count == 0
    mocked_api.links.delete_link.assert_called_with(link_to_delete)


def test_zephyr_create_links_web_urls(pytester, mock_zephyr, mock_jira, mocker):
    """
    Check that the plugin creates the links to web urls from the test case.
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

                        @pytest.mark.zephyr_testcase(urls=["example.com"])
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.links.create_web_link.assert_called_with("ANY-T200", "example.com")


@pytest.mark.parametrize(
    "url_to_keep, link_to_delete", [("www.example.com", 1000), ("www.google.com", 2000)]
)
def test_zephyr_deletes_links_web_urls(
    pytester, mock_zephyr, mock_jira, mocker, url_to_keep, link_to_delete
):
    """
    Check that the plugin deletes the links to web urls from the test case.
    """

    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "priority": {"id": 2, "self": "linkpriority/2"},
                "status": {"id": 1, "self": "linkstatus/1"},
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {"accountId": "owner123", "self": "linkuser/owner123"},
                "links": {
                    "self": "linktestcase/5",
                    "issues": [],
                    "webLinks": [
                        {"url": "www.example.com", "id": 2000},
                        {"url": "www.google.com", "id": 1000},
                    ],
                },
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

                        @pytest.mark.zephyr_testcase(urls=["{url_to_keep}"])
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.links.create_issue_link.call_count == 0
    mocked_api.links.delete_link.assert_called_with(link_to_delete)


def test_zephyr_deletes_all_links_jira_issues(pytester, mock_zephyr, mock_jira, mocker):
    """
    Check that the plugin deletes all the links to jira issue from the test case.
    """

    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "priority": {"id": 2, "self": "linkpriority/2"},
                "status": {"id": 1, "self": "linkstatus/1"},
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {"accountId": "owner123", "self": "linkuser/owner123"},
                "links": {
                    "self": "linktestcase/5",
                    "issues": [
                        {"issueId": 1000, "id": 1001},
                        {"issueId": 2000, "id": 2001},
                        {"issueId": 3000, "id": 3001},
                        {"issueId": 4000, "id": 4001},
                        {"issueId": 5000, "id": 5001},
                        {"issueId": 6000, "id": 6001},
                    ],
                    "webLinks": [],
                },
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

                        @pytest.mark.zephyr_testcase(jira_issues=[])
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.links.create_issue_link.call_count == 0
    assert mocked_api.links.delete_link.call_count == 6


def test_zephyr_deletes_all_links_web_urls(pytester, mock_zephyr, mock_jira, mocker):
    """
    Check that the plugin deletes all the links to web urls from the test case.
    """

    mocked_api = mock_zephyr
    mocker.patch(
        "zephyr.scale.cloud.endpoints.test_cases.TestCaseEndpoints.get_test_cases",
        return_value=[
            {
                "id": 5,
                "key": "ANY-T5",
                "name": "test_sth",
                "project": {"id": 1, "self": "linkproject/1"},
                "createdOn": "2020-01-01",
                "priority": {"id": 2, "self": "linkpriority/2"},
                "status": {"id": 1, "self": "linkstatus/1"},
                "folder": {"id": 100, "self": "linkfolder/100"},
                "owner": {"accountId": "owner123", "self": "linkuser/owner123"},
                "links": {
                    "self": "linktestcase/5",
                    "issues": [],
                    "webLinks": [
                        {"url": "www.example.com", "id": 1000},
                        {"url": "www.facebook.com", "id": 2000},
                        {"url": "www.twitter.com", "id": 3000},
                        {"url": "www.instagram.com", "id": 4000},
                        {"url": "www.google.com", "id": 5000},
                    ],
                },
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

                        @pytest.mark.zephyr_testcase(urls=[])
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    assert mocked_api.links.create_issue_link.call_count == 0
    assert mocked_api.links.delete_link.call_count == 5
