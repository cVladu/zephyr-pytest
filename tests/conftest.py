# -*- coding: utf-8 -*-
import pytest

pytest_plugins = "pytester"
pytest_example_dir = "examples"


@pytest.fixture
def auth_token():
    return ""  # noqa: E501


@pytest.fixture
def project_key():
    return ""


@pytest.fixture
def jira_base_url():
    return ""


@pytest.fixture
def jira_email():
    return ""


@pytest.fixture
def jira_token():
    return ""  # noqa: E501
