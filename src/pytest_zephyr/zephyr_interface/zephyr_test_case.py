# -*- coding: utf-8 -*-
from typing import Optional
from dataclasses import dataclass

TEST_STEPS_OVERWRITE = "OVERWRITE"
TEST_STEPS_APPEND = "APPEND"


@dataclass
class ZephyrTestCase:
    key: str
    name: str
    parent_folder_id: Optional[int]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ZephyrTestCase):
            return False
        return (
            self.name == other.name and self.parent_folder_id == other.parent_folder_id
        )
