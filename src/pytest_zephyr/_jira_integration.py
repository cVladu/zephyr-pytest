# -*- coding: utf-8 -*-
import requests  # type: ignore[import]
from requests.auth import HTTPBasicAuth  # type: ignore[import]


class Jira:

    def __init__(self, base_url: str, email: str, auth_token: str):
        self.base_url = base_url
        self.email = email
        self.auth_token = auth_token

    def get_issue_id(self, issue_key: str) -> int:
        url = f"{self.base_url}/rest/api/2/issue/{issue_key}"
        auth = HTTPBasicAuth(self.email, self.auth_token)
        headers = {"Accepted": "application/json"}
        response = requests.get(
            url, params={"fields": "id"}, auth=auth, headers=headers
        )
        if response.status_code != 200:
            raise ValueError(f"Jira error: {response.text}")
        return int(response.json()["id"])
