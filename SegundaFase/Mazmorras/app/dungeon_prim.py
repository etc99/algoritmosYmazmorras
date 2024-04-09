from typing import *
from .dungeon_base import DungeonBase, CellType, CellPosition, MazeCell
import networkx as nx
import random


class DungeonPrim(DungeonBase):

    def __init__(self, width: int, height: int) -> None:
        super().__init__(width, height)
        self._create_dungeon()

    def _create_dungeon(self) -> List[List[MazeCell]]:

        self.start: MazeCell = self.get_cell((random.randint(
            0, self.height - 1), random.randint(0, self.width - 1)))

        self.start.change_state(CellType.PATH)

        frontier_set: set[MazeCell] = set(
            self.get_neighbors(self.start, distance=2))

        while frontier_set:
            frontier_cell: MazeCell = random.choice(list(frontier_set))
            frontier_set.remove(frontier_cell)

            frontier_neighs: List[MazeCell] = [cell for cell in self.get_neighbors(
                frontier_cell, distance=2) if cell.state == CellType.PATH]

            connect_cell: MazeCell = frontier_neighs.pop(
                random.randint(0, len(frontier_neighs) - 1))

            frontier_cell.change_state(CellType.PATH)

            self.get_cell_between(
                frontier_cell, connect_cell).change_state(CellType.PATH)

            frontier_set.update([cell for cell in self.get_neighbors(
                frontier_cell, distance=2) if cell.state == CellType.WALL])

        self.exit: MazeCell = connect_cell

        self.exit.change_state(CellType.EXIT)
        self.start.change_state(CellType.START)

    def get_cell_between(self, origin: MazeCell, target: MazeCell) -> MazeCell:

        row_origin, col_origin = origin.get_position()
        row_target, col_target = target.get_position()

        if row_origin == row_target:
            return self.grid[row_origin][max(col_origin, col_target) - 1]
        else:
            return self.grid[max(row_origin, row_target) - 1][col_origin]