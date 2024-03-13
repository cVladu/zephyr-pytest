# -*- coding: utf-8 -*-
def test_zephyr_without_project_key(pytester):
    """Test that the plugin raises an error when no project key is provided"""

    pytester.makepyfile(
        """
        def test_sth():
            assert True
    """
    )

    result = pytester.runpytest("--zephyr")

    result.stderr.fnmatch_lines(["*ValueError: zephyr: zephyr_project_key is required"])
    assert result.ret != 1


def test_zephyr_without_auth_token_implicit_cloud(pytester):
    """Test that the plugin raises an error when no auth token is provided"""
    pytester.makeini(
        """
                         [pytest]
                         zephyr_project_key = ABC
                         """
    )
    pytester.makepyfile(
        """
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    result.stderr.fnmatch_lines(
        ["*ValueError: zephyr: zephyr_auth_token is required for cloud instance"]
    )
    assert result.ret != 1


def test_zephyr_without_auth_token_explicit_cloud(pytester):
    """Test that the plugin raises an error when no auth token is provided"""
    pytester.makeini(
        """
                         [pytest]
                         zephyr_project_key = ABC
                         zephyr_host = cloud
                         """
    )
    pytester.makepyfile(
        """
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    result.stderr.fnmatch_lines(
        ["*ValueError: zephyr: zephyr_auth_token is required for cloud instance"]
    )
    assert result.ret != 1


def test_zephyr_without_username_explicit_server(pytester):
    """Test that the plugin raises an error when no username is provided"""
    pytester.makeini(
        """
                         [pytest]
                         zephyr_project_key = ABC
                         zephyr_host = server
                         """
    )
    pytester.makepyfile(
        """
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    result.stderr.fnmatch_lines(
        ["*ValueError: zephyr: zephyr_username is required for server instance"]
    )
    assert result.ret != 1


def test_zephyr_without_password_explicit_server(pytester):
    """Test that the plugin raises an error when no password is provided"""
    pytester.makeini(
        """
                         [pytest]
                         zephyr_project_key = ABC
                         zephyr_host = server
                         zephyr_username = user
                         """
    )
    pytester.makepyfile(
        """
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    result.stderr.fnmatch_lines(
        ["*ValueError: zephyr: zephyr_password is required for server instance"]
    )
    assert result.ret != 1


def test_zephyr_invalid_host(pytester):
    """Test that the plugin raises an error when an invalid host is provided"""
    pytester.makeini(
        """
                         [pytest]
                         zephyr_project_key = ABC
                         zephyr_host = invalid
                         """
    )
    pytester.makepyfile(
        """
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    result.stderr.fnmatch_lines(["*ValueError: zephyr: Invalid zephyr_host value"])
    assert result.ret != 1
