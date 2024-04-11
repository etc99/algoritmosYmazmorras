from typing import *
from pydantic import BaseModel
from enum import Enum


class DungeonCellType(Enum):
    WALL = 0
    PATH = 1


class DungeonResponse(BaseModel):
    dungeon_cells: List[List[DungeonCellType]]
    start_position: Optional[Tuple[int, int]] = None
    exit_position: Optional[Tuple[int, int]] = None
