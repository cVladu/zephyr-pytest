# -*- coding: utf-8 -*-
import pytest

pytest_plugins = "pytester"
pytest_example_dir = "examples"


@pytest.fixture
def auth_token():
    return "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb250ZXh0Ijp7ImJhc2VVcmwiOiJodHRwczovL3RlYW0tY3AwZnNmN2JzMzVuLmF0bGFzc2lhbi5uZXQiLCJ1c2VyIjp7ImFjY291bnRJZCI6IjVjNmRiMDcyODQ5MjZjNjIzZmIxYjM0NyJ9fSwiaXNzIjoiY29tLmthbm9haC50ZXN0LW1hbmFnZXIiLCJzdWIiOiIyNmFmNmY4My0xZTg5LTMyZTgtOTRiMS1kZDc5MmE3OWU4MWIiLCJleHAiOjE3NDE2MjQ2NTEsImlhdCI6MTcxMDA4ODY1MX0.wXlPDlwoeoXfvtmmoWmX3xue3hMG-yu1vOmEGeXJp3U"  # noqa: E501


@pytest.fixture
def project_key():
    return "FP"


@pytest.fixture
def jira_base_url():
    return "https://team-cp0fsf7bs35n.atlassian.net/"


@pytest.fixture
def jira_email():
    return "catalin.alexandru.vladu@gmail.com"


@pytest.fixture
def jira_token():
    return "ATATT3xFfGF0VqvOONq5z6jE58PwyVQpOZRRApKDa_ALLPBbS883zQafDTxwnFL8s54BqnDYD-xQ7jYOKGodOj2we3ZtVRjSf9ST2iGUxlyaqAaX46EuT9UfpMX6ED0klAxP3_crWJeSpDihcTK39V-9geI9oWS5uLOI3nTe420J_mnyK4ZVkms=75702059"  # noqa: E501
