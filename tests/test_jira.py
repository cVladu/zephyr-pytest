# -*- coding: utf-8 -*-
from pytest_zephyr._jira_integration import Jira  # type: ignore[import]


def test_jira_get_issue_id_email(jira_email, jira_token, jira_base_url):
    jira = Jira(jira_base_url, jira_email, jira_token)
    issue_id = jira.get_issue_id("FP-15")
    print(issue_id)
    assert isinstance(issue_id, int)
