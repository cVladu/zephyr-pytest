# -*- coding: utf-8 -*-
from pytest_zephyr._jira_integration import Jira  # type: ignore[import]


def test_jira_get_issue_id_email(config_tokens):
    jira = Jira(
        config_tokens["jira_base_url"],
        config_tokens["jira_email"],
        config_tokens["jira_token"],
    )
    project_key = config_tokens["project_key"]
    issue_id = jira.get_issue_id(f"{project_key}-1")
    assert isinstance(issue_id, int)
