# -*- coding: utf-8 -*-


def test_zephyr_without_project_key(pytester, config_tokens):
    """Test that the plugin raises an error when no project key is provided"""

    pytester.makepyfile(
        """
        def test_sth():
            assert True
    """
    )

    result = pytester.runpytest("--zephyr")

    result.stderr.fnmatch_lines(
        "*zephyr: The following mandatory params not found in pytest ini file or sys env vars:"
    )
    result.stderr.fnmatch_lines("*zephyr_project_key*")
    result.stderr.fnmatch_lines("*zephyr_auth_token*")
    result.stderr.fnmatch_lines("*zephyr_jira_base_url*")
    result.stderr.fnmatch_lines("*zephyr_jira_email*")
    result.stderr.fnmatch_lines("*zephyr_jira_token*")
    assert result.ret != 1


def test_zephyr_without_auth_token(pytester, config_tokens):
    """Test that the plugin raises an error when no auth token is provided"""
    project_key = config_tokens["project_key"]
    pytester.makeini(
        f"""
                         [pytest]
                         zephyr_project_key = {project_key}
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
        "*zephyr: The following mandatory params not found in pytest ini file or sys env vars:"
    )
    result.stderr.fnmatch_lines("*zephyr_auth_token*")
    result.stderr.fnmatch_lines("*zephyr_jira_base_url*")
    result.stderr.fnmatch_lines("*zephyr_jira_email*")
    result.stderr.fnmatch_lines("*zephyr_jira_token*")
    assert result.ret != 0


def test_zephyr_without_jira_base_url(pytester, config_tokens):
    """Test that the plugin does not raise an error when all required fields are provided"""
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    pytester.makeini(
        f"""
                         [pytest]
                         zephyr_project_key = {project_key}
                         zephyr_auth_token = {auth_token}
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
        "*zephyr: The following mandatory params not found in pytest ini file or sys env vars:"
    )
    result.stderr.fnmatch_lines("*zephyr_jira_base_url*")
    result.stderr.fnmatch_lines("*zephyr_jira_email*")
    result.stderr.fnmatch_lines("*zephyr_jira_token*")
    assert result.ret != 0


def test_zephyr_without_jira_username(pytester, config_tokens):
    """Test that the plugin does not raise an error when all required fields are provided"""
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    pytester.makeini(
        f"""
                         [pytest]
                         zephyr_project_key = {project_key}
                         zephyr_auth_token = {auth_token}
                         zephyr_jira_base_url = {jira_base_url}
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
        "*zephyr: The following mandatory params not found in pytest ini file or sys env vars:"
    )
    result.stderr.fnmatch_lines("*zephyr_jira_email*")
    result.stderr.fnmatch_lines("*zephyr_jira_token*")
    assert result.ret != 0


def test_zephyr_without_jira_token(pytester, config_tokens):
    """Test that the plugin does not raise an error when all required fields are provided"""
    project_key = config_tokens["project_key"]
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    pytester.makeini(
        f"""
                         [pytest]
                         zephyr_project_key = {project_key}
                         zephyr_auth_token = {auth_token}
                         zephyr_jira_base_url = {jira_base_url}
                         zephyr_jira_email = {jira_email}
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
        "*zephyr: The following mandatory params not found in pytest ini file or sys env vars:"
    )
    result.stderr.fnmatch_lines("*zephyr_jira_token*")
    assert result.ret != 0


def test_zephyr_strict_default_false_unk_project_key(pytester, config_tokens):
    """
    Test that the plugin emits a warning when the strict option is set to False
    """
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
            [pytest]
            zephyr_project_key = UNK
            zephyr_auth_token = {auth_token}
            zephyr_jira_base_url = {jira_base_url}
            zephyr_jira_email = {jira_email}
            zephyr_jira_token = {jira_token}
            """
    )
    pytester.makepyfile(
        """
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    result.stdout.fnmatch_lines("*PytestConfigWarning: Could not connect to Zephyr*")
    assert result.ret == 0


def test_zephyr_strict_default_false_unk_auth_token(pytester, config_tokens):
    """
    Test that the plugin emits a warning when the strict option is set to False
    """
    project_key = config_tokens["project_key"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
            [pytest]
            zephyr_project_key = {project_key}
            zephyr_auth_token = UNK
            zephyr_jira_base_url = {jira_base_url}
            zephyr_jira_email = {jira_email}
            zephyr_jira_token = {jira_token}
            """
    )
    pytester.makepyfile(
        """
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    result.stdout.fnmatch_lines("*PytestConfigWarning: Could not connect to Zephyr*")
    assert result.ret == 0


def test_zephyr_strict_false_unk_project_key(pytester, config_tokens):
    """
    Test that the plugin emits a warning when the strict option is set to False
    """
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
            [pytest]
            zephyr_project_key = UNK
            zephyr_auth_token = {auth_token}
            zephyr_jira_base_url = {jira_base_url}
            zephyr_jira_email = {jira_email}
            zephyr_jira_token = {jira_token}
            zephyr_strict = False
            """
    )
    pytester.makepyfile(
        """
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    result.stdout.fnmatch_lines("*PytestConfigWarning: Could not connect to Zephyr*")
    assert result.ret == 0


def test_zephyr_strict_false_unk_auth_token(pytester, config_tokens):
    """
    Test that the plugin emits a warning when the strict option is set to False
    """
    project_key = config_tokens["project_key"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
            [pytest]
            zephyr_project_key = {project_key}
            zephyr_auth_token = UNK
            zephyr_jira_base_url = {jira_base_url}
            zephyr_jira_email = {jira_email}
            zephyr_jira_token = {jira_token}
            zephyr_strict = False
            """
    )
    pytester.makepyfile(
        """
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    result.stdout.fnmatch_lines("*PytestConfigWarning: Could not connect to Zephyr*")
    assert result.ret == 0


def test_zephyr_strict_true_unk_project_key(pytester, config_tokens):
    """
    Test that the plugin raises an error when the strict option is set to True
    """
    auth_token = config_tokens["auth_token"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
            [pytest]
            zephyr_project_key = UNK
            zephyr_auth_token = {auth_token}
            zephyr_jira_base_url = {jira_base_url}
            zephyr_jira_email = {jira_email}
            zephyr_jira_token = {jira_token}
            zephyr_strict = True
            """
    )
    pytester.makepyfile(
        """
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    result.stderr.fnmatch_lines("*zephyr: Could not connect to Zephyr*")
    assert result.ret != 0


def test_zephyr_strict_true_unk_auth_token(pytester, config_tokens):
    """
    Test that the plugin raises an error when the strict option is set to True
    """
    project_key = config_tokens["project_key"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_base_url = config_tokens["jira_base_url"]
    jira_email = config_tokens["jira_email"]
    jira_token = config_tokens["jira_token"]
    pytester.makeini(
        f"""
            [pytest]
            zephyr_project_key = {project_key}
            zephyr_auth_token = UNK
            zephyr_jira_base_url = {jira_base_url}
            zephyr_jira_email = {jira_email}
            zephyr_jira_token = {jira_token}
            zephyr_strict = True
            """
    )
    pytester.makepyfile(
        """
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    result.stderr.fnmatch_lines("*zephyr: Could not connect to Zephyr*")
    assert result.ret != 0


def test_zephyr_all_required_fields(pytester, config_tokens):
    """Test that the plugin does not raise an error when all required fields are provided"""
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
                         """
    )
    pytester.makepyfile(
        """
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
