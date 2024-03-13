# -*- coding: utf-8 -*-
from typing import List, Optional
from dataclasses import dataclass, field

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
