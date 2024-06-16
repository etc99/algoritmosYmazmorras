
from typing import *
from abc import ABC, abstractmethod
from enum import Enum
import random

CellPosition = Tuple[int, int]


class CellType(Enum):
    WALL = 0
    PATH = 1


class MazeCell:

    def __init__(self, row: int, column: int, state: CellType = CellType.WALL) -> None:
        self.row: int = row
        self.column: int = column
        self.state: CellType = state

    def __str__(self) -> str:
        cell_type_mapping: Dict[CellType, str] = {
            CellType.PATH: ".",
            CellType.WALL: '▓'
        }

        return cell_type_mapping[self.state]

    def get_position(self) -> CellPosition:
        return (self.row, self.column)

    def change_state(self, new_state: CellType) -> None:
        self.state = new_state

    def __repr__(self) -> str:
        return f"[{self.row}-{self.column}:{self.state.value}]"

    def __hash__(self) -> int:
        return hash((self.row, self.column))
    
    def __eq__(self, value: object) -> bool:
        return all((self.row == value.row, self.column == value.column, self.state == value.state))


class DungeonBase(ABC):

    def __init__(self, **kwargs) -> None:
        self.grid: List[List[MazeCell]] = []

    @abstractmethod
    def _create_dungeon(self) -> None:
        pass


    def get_neighbors(self, cell: MazeCell, distance: int = 1) -> List[MazeCell]:

        position = cell.get_position()
        directions: Dict[str, Tuple] = {
            "UP": (distance, 0),
            "DOWN": (-distance, 0),
            "LEFT": (0, -distance),
            "RIGHT": (0, distance)
        }

        neigh: List[MazeCell] = []

        for direction in directions.values():
            check_position: CellPosition = (
                position[0] + direction[0], position[1] + direction[1])

            if self.inside_map(check_position):

                neigh.append(self.get_cell(check_position))

        return neigh

    def get_cell(self, position: CellPosition) -> MazeCell:
        return self.grid[position[0]][position[1]]

    def inside_map(self, position: CellPosition) -> bool:
        return (0 <= position[0] < self._height) and (0 <= position[1] < self._width)

    def __str__(self) -> str:
        dungeon_str: str = ''

        for i,row in enumerate(self.grid):
            for  cell in row:
                dungeon_str += str(cell)
            dungeon_str += str(i) + "\n"

        return dungeon_str
    
    def serialize_grid(self):

        return [[ cell.state.value for cell in row] for row in self.grid]
        

class SizeableDungeon(DungeonBase):

    def __init__(self, width: int, height: int, seed: int | None = None, **kwargs) -> None:
        self._width: int = int(width)
        self._height: int = int(height)
        self.seed: int = int(seed) if seed else random.randint(0,1000)
        self.steps: List[CellPosition] = []
        random.seed(self.seed)

        maze_list: List[List[MazeCell]] = []

        for i in range(self._height):
            new_row: List[MazeCell] = []
            for j in range(self._width):
                new_row.append(MazeCell(i, j))
            maze_list.append(new_row)
        self.grid = maze_list
        self._create_dungeon()

    @property
    def height(self) -> int:
        return self._height
    
    @property
    def width(self) -> int:
        return self._width