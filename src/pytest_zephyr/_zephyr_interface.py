# -*- coding: utf-8 -*-
from typing import List, Optional, Dict
from dataclasses import dataclass, field

TEST_STEPS_OVERWRITE = "OVERWRITE"
TEST_STEPS_APPEND = "APPEND"


TEST_CASE_FOLDER_TYPE = "TEST_CASE"
TEST_PLAN_FOLDER_TYPE = "TEST_PLAN"
TEST_CYCLE_FOLDER_TYPE = "TEST_CYCLE"


@dataclass
class Folder:
    name: str
    id: Optional[int]
    children: List["Folder"] = field(default_factory=list)

    def search_by_name(self, name: str) -> Optional["Folder"]:
        if self.name == name:
            return self
        for child in self.children:
            ret = child.search_by_name(name)
            if ret:
                return ret
        return None

    def search_by_id(self, id: int) -> Optional["Folder"]:
        if self.id == id:
            return self
        for child in self.children:
            ret = child.search_by_id(id)
            if ret:
                return ret
        return None

    def add_child(self, child: "Folder") -> None:
        self.children.append(child)

    def pprint(self, indent: int = 0) -> None:
        print(f"{' ' * indent}{self.name} ({self.id})")
        for child in self.children:
            child.pprint(indent + 4)


class ZephyrTestCase:

    # TODO:
    # priorityName and statusName can be passed to this init
    # The mapping will be done internally
    # Find a way to have the mapping as an interface
    def __init__(
        self,
        id: int = 0,
        key: str = "",
        name: str = "",
        project_id: int = 0,
        createdOn: str = "",
        objective: str = "",
        precondition: str = "",
        estimatedTime: int = 0,
        labels: Optional[List[str]] = None,
        priority_id: int = 0,
        status_id: int = 0,
        folder_id: Optional[int] = None,
        ownerId: Optional[str] = None,
        jira_issues: Optional[List[int]] = None,
        urls: Optional[List[str]] = None,
        customFields: Optional[Dict[str, str]] = None,
        jira_issues_links: Optional[Dict[int, int]] = None,
        urls_links: Optional[Dict[str, int]] = None,
        **kwargs,
    ):
        self.id = id
        self.key = key
        self.name = name
        self.project_id = project_id
        self.createdOn = createdOn
        self.objective = objective
        self.precondition = precondition
        self.estimatedTime = estimatedTime
        if labels is None:
            labels = []
        self.labels = labels
        self.priority_id = priority_id
        self.status_id = status_id
        self.folder_id = folder_id
        self.ownerId = ownerId
        if jira_issues is None:
            jira_issues = []
        self.jira_issues = jira_issues
        if urls is None:
            urls = []
        self.urls = urls
        if customFields is None:
            customFields = {}
        self.customFields = customFields
        if jira_issues_links is None:
            jira_issues_links = {}
        self.jira_issues_links = jira_issues_links
        if urls_links is None:
            urls_links = {}
        self.urls_links = urls_links

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ZephyrTestCase):
            return False
        return self.name == other.name and self.folder_id == other.folder_id

    def to_dict(self) -> dict:
        ret_dict = {
            "id": self.id,
            "key": self.key,
            "name": self.name,
            "project_id": self.project_id,
            "createdOn": self.createdOn,
            "objective": self.objective,
            "precondition": self.precondition,
            "estimatedTime": self.estimatedTime,
            "labels": self.labels,
            "priority_id": self.priority_id,
            "status_id": self.status_id,
            "folder": {"id": self.folder_id},
            "jira_issues": self.jira_issues,
            "urls": self.urls,
            "customFields": self.customFields,
        }
        if self.ownerId:
            ret_dict["owner"] = {"accountId": self.ownerId}
        return ret_dict

    def __repr__(self) -> str:
        return f"ZephyrTestCase(id={self.id}, key={self.key}, name={self.name}, project_id={self.project_id}, createdOn={self.createdOn}, objective={self.objective}, precondition={self.precondition}, estimatedTime={self.estimatedTime}, labels={self.labels}, priority_id={self.priority_id}, status_id={self.status_id}, folder_id={self.folder_id}, ownerId={self.ownerId}, jira_issues={self.jira_issues}, urls={self.urls})"  # noqa: E501
