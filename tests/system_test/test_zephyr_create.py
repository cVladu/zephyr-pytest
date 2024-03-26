# -*- coding: utf-8 -*-
import os
import pytest


def test_zephyr_making_folder_root(pytester, config_tokens):
    """
    Check that the plugin can handle tests at the same level as the root folder
    """
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
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """
                        import pytest

                        @pytest.mark.zephyr_testcase
                        def test_first_level():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_making_folder_root_with_testclass(pytester, config_tokens):
    """
    Check that the plugin can handle tests at the same level as the root folder
    """
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
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """
                        import pytest

                        class TestClass:
                            @pytest.mark.zephyr_testcase
                            def test_first_level(self):
                                assert True
                            @pytest.mark.zephyr_testcase
                            def test_second_level(self):
                                assert True
                        """
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_making_folders(
    pytester,
    config_tokens,
    testdir,
):
    """
    Check that the plugin created the folders in Zephyr Scale
    """
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
zephyr_strict = True
                         """
    )
    testdir.mkdir("folder_0")
    testdir.mkdir("folder_0/subfolder_0")
    testdir.mkdir("folder_0/subfolder_1")
    testdir.mkdir("folder_0/subfolder_1/subsubfolder_0")  # noqa: E501
    testdir.mkdir("folder_1")
    testdir.mkdir("folder_1/subfolder_0")
    with open(
        os.path.join(testdir.tmpdir, "folder_0/test_0.py"),
        "w",
    ) as f:
        f.write(
            """
import pytest

@pytest.mark.zephyr_testcase
def test_depth():
    assert True

def test_depth_2():
    assert True
                """
        )
    with open(
        os.path.join(
            testdir.tmpdir,
            "folder_0/subfolder_1/test_1.py",  # noqa: E501
        ),
        "w",
    ) as f:
        f.write(
            """
import pytest

@pytest.mark.zephyr_testcase
def test_depth_something():
    assert True
                """
        )
    with open(
        os.path.join(
            testdir.tmpdir,
            "folder_1/subfolder_0/test_2.py",  # noqa: E501
        ),
        "w",
    ) as f:
        f.write(
            """
import pytest

@pytest.mark.zephyr_testcase
def test_depth_something_else():
    assert True
                """
        )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_making_folders_existing(
    pytester,
    config_tokens,
    testdir,
):
    """
    Check that the plugin does not create the folders in Zephyr Scale if they already exist
    """
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
zephyr_strict = True
                         """
    )
    testdir.mkdir("test_examples")
    testdir.mkdir("test_examples/test_a")
    final_path = testdir.mkdir("test_examples/test_a/test_b")  # noqa: E501
    with open(final_path.join("test_c.py"), "w") as f:
        f.write(
            """
import pytest

@pytest.mark.zephyr_testcase
def test_depth():
    assert True
    """
        )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_making_folders_mix(
    pytester,
    config_tokens,
    testdir,
):
    """
    Check that the plugin creates the folders in Zephyr Scale if they do not exist
    """
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
zephyr_strict = True
                         """
    )
    testdir.mkdir("test_mix")
    testdir.mkdir("test_mix/test_a")
    final_path = testdir.mkdir("test_mix/test_a/test_b")  # noqa: E501
    with open(final_path.join("test_c.py"), "w") as f:
        f.write(
            """
def test_depth():
    assert True
    """
        )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0

    testdir.mkdir("test_mix/test_d")
    with open(
        testdir.tmpdir.join("test_mix/test_a/test_something.py"),  # noqa: E501
        "w",
    ) as f:
        f.write(
            """
import pytest

@pytest.mark.zephyr_testcase
def test_depth():
    assert True
    """
        )
    with open(
        testdir.tmpdir.join("test_mix/test_a/test_something_else.py"),  # noqa: E501
        "w",
    ) as f:
        f.write(
            """
import pytest

@pytest.mark.zephyr_testcase
def test_depth():
    assert True
    """
        )
    with open(
        testdir.tmpdir.join("test_mix/test_d/test_d_something.py"),  # noqa: E501
        "w",
    ) as f:
        f.write(
            """
import pytest

@pytest.mark.zephyr_testcase
def test_depth():
    assert True
    """
        )

    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_creating_parametrized_test(
    pytester,
    config_tokens,
    testdir,
):
    """
    Check that the plugin creates the test case in Zephyr Scale if it does not exist
    """
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
zephyr_strict = True
                         """
    )
    testdir.mkdir("test_parametrized")
    final_path = testdir.mkdir("test_parametrized/test_a")  # noqa: E501
    with open(final_path.join("test_b.py"), "w") as f:
        f.write(
            """
import pytest


@pytest.mark.zephyr_testcase
@pytest.mark.parametrize(\"input, expected\", [
    (1, 2),
    (3, 4),
    (5, 6)
])
def test_depth(input, expected):
    assert input + 1 == expected """
        )
    result = pytester.runpytest(
        "--zephyr",
        "--zephyr-no-publish",
        "test_parametrized",
    )
    assert result.ret == 0


def test_zephyr_creating_with_marker(pytester, config_tokens):
    """
    Check that the plugin correctly creates the test case in zephyr given the marker
    """
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
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


project_key = "FP"


@pytest.mark.parametrize(
    "jira_issues",
    [
        [f"{project_key}-12"],
        [f"{project_key}-12", f"{project_key}-13"],
        [f"{project_key}-12", f"{project_key}-13", f"{project_key}-14"],
        ["12"],
        ["13", "14"],
        ["12", "13", "14"],
        [f"{project_key}-12", "13", "14"],
        ["12", f"{project_key}-13", "14"],
        ["12", "13", f"{project_key}-14"],
    ],
)
def test_zephyr_creating_with_jira_issues(pytester, config_tokens, jira_issues):
    """
    Check that the plugin correctly links the issues to the created test case
    """
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
zephyr_strict = True
                         """
    )
    test_name = "test_sth" + "_".join(jira_issues)
    test_name = test_name.replace("-", "_")
    pytester.makepyfile(
        f"""  # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\",jira_issues={jira_issues})
def {test_name}():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_creating_with_marker_extra_kwarg(pytester, config_tokens):
    """
    Check that the plugin correctly creates the test case in zephyr
    given the marker with extra kwarg
    """
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
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """# noqa: E501
import pytest
@pytest.mark.zephyr_testcase(extra_kwarg=\"This should be ignored\", objective=\"The objective of the test case\", precondition="A precondition", labels=[\"label_1\", \"label_2\"], estimatedTime=3600000, priorityName=\"High\", statusName=\"Approved\", ownerId=\"5c6db07284926c623fb1b347\")
def test_sth():
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_creating_with_teststeps_docstring(pytester, config_tokens):
    """
    Check that the plugin correctly creates the test steps from __doc__
    """
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
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """
import pytest
@pytest.mark.zephyr_testcase(test_steps="doc")
def test_sth():
    \"\"\"This is a test case
    Test steps:
        1. Do something
        2. Do something else
        3. Do something else again
    \"\"\"
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_creating_with_teststeps_list(pytester, config_tokens):
    """
    Check that the plugin correctly creates the test steps from list
    """
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
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """ # noqa: E501
import pytest
@pytest.mark.zephyr_testcase(test_steps=[{"step": "Do something", "expected": "Something happened"}, {"step": "Do something without expectation"}, {"step": "Do final thing", "expected": "Final thing happened"}])
def test_sth():
    \"\"\"This is a test case
    Test steps:
        1. Do something
        2. Do something else
        3. Do something else again
    \"\"\"
    assert True
"""
    )
    result = pytester.runpytest("--zephyr", "--zephyr-no-publish")
    assert result.ret == 0


def test_zephyr_creating_test_cycle_default_name(pytester, config_tokens):
    """
    Check that the plugin correctly creates the test cycle given no name
    """
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
zephyr_strict = True
                         """
    )
    pytester.makepyfile(
        """
import pytest
@pytest.mark.zephyr_testcase(test_steps="doc")
def test_sth():
    \"\"\"This is a test case
    Test steps:
        1. Do something
        2. Do something else
        3. Do something else again
    \"\"\"
    assert True
"""
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0


def test_zephyr_creating_test_cycle_given_name(pytester, config_tokens):
    """
    Check that the plugin correctly creates the test cycle given only name
    """
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
zephyr_strict = True
zephyr_testcycle_name = "Custom Name"
                         """
    )
    pytester.makepyfile(
        """
import pytest
@pytest.mark.zephyr_testcase(test_steps="doc")
def test_sth():
    \"\"\"This is a test case
    Test steps:
        1. Do something
        2. Do something else
        3. Do something else again
    \"\"\"
    assert True
"""
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0


def test_zephyr_creating_test_cycle_given_description(pytester, config_tokens):
    """
    Check that the plugin correctly creates the test cycle given only description
    """
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
zephyr_strict = True
zephyr_testcycle_description = Custom Description. Is this shown?
                         """
    )
    pytester.makepyfile(
        """
import pytest
@pytest.mark.zephyr_testcase(test_steps="doc")
def test_sth():
    \"\"\"This is a test case
    Test steps:
        1. Do something
        2. Do something else
        3. Do something else again
    \"\"\"
    assert True
"""
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0


def test_zephyr_creating_test_cycle_given_name_and_description(
    pytester,
    config_tokens,
):
    """
    Check that the plugin correctly creates the test cycle given name and description
    """
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
zephyr_strict = True
zephyr_testcycle_name = Custom Name 2
zephyr_testcycle_description = Custom Description. Is this shown?
                         """
    )
    pytester.makepyfile(
        """
import pytest
@pytest.mark.zephyr_testcase(test_steps="doc")
def test_sth():
    \"\"\"This is a test case
    Test steps:
        1. Do something
        2. Do something else
        3. Do something else again
    \"\"\"
    assert True
"""
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0


def test_zephyr_creating_test_cycle_link_to_test_plan(pytester, config_tokens):
    """
    Check that the plugin correctly creates the test cycle and links to test plan
    """
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
zephyr_strict = True
zephyr_testcycle_name = Test Cycle Linked To Test Plan
zephyr_testcycle_description = Custom Description. Is this shown?
zephyr_testplan_id = {project_key}-P1
"""
    )
    pytester.makepyfile(
        """
import pytest
@pytest.mark.zephyr_testcase(test_steps="doc")
def test_sth():
    \"\"\"This is a test case
    Test steps:
        1. Do something
        2. Do something else
        3. Do something else again
    \"\"\"
    assert True
"""
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0


def test_zephyr_creating_test_cycle_link_to_test_plan_without_project_key(
    pytester, config_tokens
):
    """
    Check that the plugin correctly creates the test cycle and links to test plan
    """
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
zephyr_strict = True
zephyr_testcycle_name = Test Cycle Linked To Test Plan
zephyr_testcycle_description = Custom Description. Is this shown?
zephyr_testplan_id = P1
"""
    )
    pytester.makepyfile(
        """
import pytest
@pytest.mark.zephyr_testcase(test_steps="doc")
def test_sth():
    \"\"\"This is a test case
    Test steps:
        1. Do something
        2. Do something else
        3. Do something else again
    \"\"\"
    assert 1 + 2 == 3
"""
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0


def test_zephyr_creating_test_cycle_owner(pytester, config_tokens):
    """
    Check that the plugin correctly creates the test cycle with the given owner
    """
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
zephyr_strict = True
zephyr_testcycle_name = Test Cycle With Owner
zephyr_testcycle_description = Custom Description. Is this shown?
zephyr_testplan_id = P1
"""
    )
    pytester.makepyfile(
        """
import pytest
@pytest.mark.zephyr_testcase(test_steps="doc")
def test_sth():
    \"\"\"This is a test case
    Test steps:
        1. Do something
        2. Do something else
        3. Do something else again
    \"\"\"
    assert 1 + 2 == 3
"""
    )
    result = pytester.runpytest(
        "--zephyr", "--zephyr-owner-id=5c6db07284926c623fb1b347"
    )
    assert result.ret == 0
