# How to test the code

To run all the mock tests and linters, use the following command:
```bash
tox
```
In order to run the system tests (connecting to Zephyr scale), a `config_tokens.json` file needs to be created in the root repository. This file should contain the following information:
```json
{
  "auth_token" : "<The auth token for the Zephyr Scale API>",
  "project_key": "<The project key for the Zephyr Scale project>",
  "jira_base_url": "The base URL for the Jira instance",
  "jira_email": "The email for the Jira user",
  "jira_token": "The token for the Jira user"
}
```
Then, run the following command:
```bash
tox -e system
```
