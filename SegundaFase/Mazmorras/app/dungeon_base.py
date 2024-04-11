
from typing import *
from abc import ABC, abstractmethod
from enum import Enum
from .dungeon_response import DungeonResponse, DungeonCellType

CellPosition = Tuple[int, int]


class CellType(Enum):
    PATH = 1
    WALL = 2
    START = 3
    EXIT = 4


class MazeCell:

    def __init__(self, row: int, column: int, state: CellType = CellType.WALL) -> None:
        self.row: int = row
        self.column: int = column
        self.state: CellType = state
        self.start: MazeCell
        self.exit: MazeCell

    def __str__(self) -> str:
        cell_type_mapping: Dict[CellType, str] = {
            CellType.PATH: ".",
            CellType.WALL: '▓',
            CellType.START: "O",
            CellType.EXIT: "X"
        }

        return cell_type_mapping[self.state]

    def get_position(self) -> CellPosition:
        return (self.row, self.column)

    def change_state(self, new_state: CellType) -> None:
        self.state = new_state

    def __repr__(self) -> str:
        return f"[{self.row}-{self.column}]:{self.state.name}"

    def __hash__(self) -> int:
        return hash((self.row, self.column))


class DungeonBase(ABC):

    def __init__(self, width: int, height: int) -> None:
        self.width: int = width
        self.height: int = height

        maze_list: List[List[MazeCell]] = []

        for i in range(self.height):
            new_row: List[MazeCell] = []
            for j in range(self.width):
                new_row.append(MazeCell(i, j))
            maze_list.append(new_row)
        self.grid: List[List[MazeCell]] = maze_list

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
        return (0 <= position[0] < self.height) and (0 <= position[1] < self.width)

    def __str__(self) -> str:
        dungeon_str: str = ''

        for row in self.grid:
            for cell in row:
                dungeon_str += str(cell)
            dungeon_str += "\n"

        return dungeon_str

    def to_dungeon_response(self) -> DungeonResponse:

        dungeon_matrix: List[List[DungeonCellType]] = []
        # Iteramos sobre la mazmorra
        for row in self.grid:
            row_list: List[DungeonCellType] = []
            for cell in row:
                if cell.state == CellType.WALL:
                    row_list.append(DungeonCellType.WALL)
                else:
                    row_list.append(DungeonCellType.PATH)
            dungeon_matrix.append(row_list)

        return DungeonResponse(dungeon_cells=dungeon_matrix,
                                start_position=self.start.get_position() if self.start else None,
                                exit_position=self.exit.get_position() if self.exit else None)

