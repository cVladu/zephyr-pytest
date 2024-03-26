# -*- coding: utf-8 -*-
import os
from pytest_zephyr._zephyr_interface import TEST_CASE_FOLDER_TYPE


def test_zephyr_creates_folder(pytester, mock_zephyr, mocker):
    """
    Check that the plugin creates a folder in Zephyr Scale (Mocked)
    """
    mocked_api = mock_zephyr
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email = user@mail.com
zephyr_jira_token = TOKEN
zephyr_strict = True
        """
    )
    pytester.makepyfile(
        """
                        import pytest

                        @pytest.mark.zephyr_testcase
                        def test_sth():
                            assert True
                        """
    )
    result = pytester.runpytest("--zephyr")
    assert result.ret == 0
    mocked_api.folders.create_folder.assert_called_once_with(
        "test_zephyr_creates_folder.py", "ANY", TEST_CASE_FOLDER_TYPE, parentId=None
    )


def test_zephyr_create_folder_tree(pytester, mock_zephyr, mocker, testdir):
    """
    Check that the plugin creates a folder tree in Zephyr Scale (Mocked)
    """
    mocked_api = mock_zephyr
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email =  user@email.com
zephyr_jira_token = TOKEN
zephyr_strict = True
       """
    )

    testdir.mkdir("folder_0")
    with open(
        os.path.join(testdir.tmpdir, "folder_0/test_file.py"),
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
    result = testdir.runpytest("--zephyr")
    assert result.ret == 0
    assert (
        mocked_api.folders.create_folder.call_count == 2
    ), f"Called with {mocked_api.folders.create_folder.call_args_list}"
    mocked_api.folders.create_folder.assert_called_with(
        "test_file.py", "ANY", TEST_CASE_FOLDER_TYPE, parentId=100
    )


def test_zephyr_no_create_folder_existent(pytester, mock_zephyr, mocker, testdir):
    """
    Check that the plugin does not create already existing folders
    """
    mocked_api = mock_zephyr
    # repatch get_folders to return a folder tree
    mocker.patch(
        "zephyr.scale.cloud.endpoints.folders.FolderEndpoints.get_folders",
        return_value=[
            {"id": 1, "folderType": "TEST_CASE", "name": "folder_1", "parentId": None},
            {"id": 2, "folderType": "TEST_CASE", "name": "sub_folder_1", "parentId": 1},
            {"id": 3, "folderType": "TEST_CYCLE", "name": "cycle_1", "parentId": None},
            {"id": 4, "folderType": "TEST_CYCLE", "name": "sub_cycle_1", "parentId": 3},
            {"id": 5, "folderType": "TEST_CASE", "name": "folder_2", "parentId": None},
            {"id": 6, "folderType": "TEST_CASE", "name": "sub_folder_2", "parentId": 5},
            {
                "id": 7,
                "folderType": "TEST_CASE",
                "name": "test_file_0.py",
                "parentId": 1,
            },
            {
                "id": 8,
                "folderType": "TEST_CASE",
                "name": "test_file_1.py",
                "parentId": 2,
            },
            {
                "id": 9,
                "folderType": "TEST_CASE",
                "name": "test_file_2.py",
                "parentId": 5,
            },
            {
                "id": 10,
                "folderType": "TEST_CASE",
                "name": "test_file_3.py",
                "parentId": 6,
            },
        ],
    )
    pytester.makeini(
        """
[pytest]
zephyr_project_key = ANY
zephyr_auth_token = KNWON
zephyr_jira_base_url = example.com
zephyr_jira_email =  user@email.com
zephyr_jira_token = TOKEN
zephyr_strict = True
       """
    )

    testdir.mkdir("folder_1")
    testdir.mkdir("folder_1/sub_folder_1")
    testdir.mkdir("folder_2")
    testdir.mkdir("folder_2/sub_folder_2")
    with open(
        os.path.join(testdir.tmpdir, "folder_1/test_file_0.py"),
        "w",
    ) as f:
        f.write(
            """
import pytest

@pytest.mark.zephyr_testcase
def test_folder_1():
    assert True
                """
        )
    with open(
        os.path.join(testdir.tmpdir, "folder_1/sub_folder_1/test_file_1.py"),
        "w",
    ) as f:
        f.write(
            """
import pytest

@pytest.mark.zephyr_testcase
def test_sub_folder_1():
    assert True
                """
        )
    with open(
        os.path.join(testdir.tmpdir, "folder_2/test_file_2.py"),
        "w",
    ) as f:
        f.write(
            """
import pytest

@pytest.mark.zephyr_testcase
def test_folder_2():
    assert True
                """
        )
    with open(
        os.path.join(testdir.tmpdir, "folder_2/sub_folder_2/test_file_3.py"),
        "w",
    ) as f:
        f.write(
            """
import pytest

@pytest.mark.zephyr_testcase
def test_sub_folder_2():
    assert True
                """
        )
    result = testdir.runpytest("--zephyr")
    assert result.ret == 0
    assert (
        mocked_api.folders.create_folder.call_count == 0
    ), f"Called with {mocked_api.folders.create_folder.call_args_list}"
