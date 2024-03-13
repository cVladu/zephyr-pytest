# -*- coding: utf-8 -*-
import pytest
from zephyr import ZephyrScale


def _fmt_zephyr_error(msg: str):
    return ValueError(f"zephyr: {msg}")


class ZephyrManager:
    def __init__(self, project_key: str):
        self.zephyr_api = None
        self.project_key = project_key


class ZephyrManagerCloud(ZephyrManager):
    def __init__(self, auth_token: str, base_url: str, project_key: str):
        super().__init__(project_key)
        self.zephyr_api = ZephyrScale(base_url, token=auth_token)


class ZephyrManagerServer(ZephyrManager):
    def __init__(self, username: str, password: str, base_url: str, project_key: str):
        super().__init__(project_key)
        auth = {"username": username, "password": password}
        self.zephyr_api = ZephyrScale.server_api(base_url, **auth)


def pytest_configure(config: pytest.Config):
    if not config.option.zephyr:
        return

    project_key = config.getini("zephyr_project_key")
    if not project_key:
        raise _fmt_zephyr_error("zephyr_project_key is required")
    base_url = config.getini("zephyr_base_url")
    zephyr_host = config.getini("zephyr_host") or "cloud"
    if zephyr_host == "cloud":
        auth_token = config.getini("zephyr_auth_token")
        if not auth_token:
            raise _fmt_zephyr_error("zephyr_auth_token is required for cloud instance")
        zephyr_manager = ZephyrManagerCloud(auth_token, base_url, project_key)
    elif zephyr_host == "server":
        username = config.getini("zephyr_username")
        if not username:
            raise _fmt_zephyr_error("zephyr_username is required for server instance")
        password = config.getini("zephyr_password")
        if not password:
            raise _fmt_zephyr_error("zephyr_password is required for server instance")
        zephyr_manager = ZephyrManagerServer(username, password, base_url, project_key)
    else:
        raise _fmt_zephyr_error("Invalid zephyr_host value")

    config.pluginmanager.register(zephyr_manager)


def pytest_addoption(parser):
    parser.addoption("--zephyr", action="store_true", help="Enable Zephyr integration")
    parser.addini("zephyr_project_key", help="Zephyr project key", type="string")
    parser.addini("zephyr_base_url", help="Zephyr base url", type="string")
    parser.addini(
        "zephyr_host", help="Zephyr host type: cloud or server", type="string"
    )
    parser.addini(
        "zephyr_auth_token", help="Zephyr auth token for cloud instance", type="string"
    )
    parser.addini(
        "zephyr_username", help="Zephyr username for server instance", type="string"
    )
    parser.addini(
        "zephyr_password", help="Zephyr password for server instance", type="string"
    )
