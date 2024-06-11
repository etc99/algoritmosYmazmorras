from typing import List
from .dungeon_base import *
from typing import *
import random
import sys

class DungeonDFS(SizeableDungeon):

    def __init__(self, width: int, height: int, seed: int | None = None) -> None:
        super().__init__(width, height, seed)

    def _create_dungeon(self) -> None:
        self.start: MazeCell = self.get_cell(
            (random.randint(0, self._height - 1), random.randint(0, self._width - 1)))

        self.make_paths(self.start)


    def make_paths(self, cell: MazeCell, from_cell: Optional[MazeCell] = None) -> None:

        cell.change_state(CellType.PATH)

        if from_cell:
            cell_to_change: MazeCell = self.get_cell_between(cell, from_cell)
            cell_to_change.change_state(CellType.PATH)
            self.steps.append(cell_to_change.get_position())

        random_neighs = self.get_neighbors(cell, distance=2)
        random.shuffle(random_neighs)

        for neigh in random_neighs:

            self.exit: MazeCell = neigh

            if neigh.state == CellType.PATH:
                continue

            self.make_paths(neigh, cell)

    def get_cell_between(self, origin: MazeCell, target: MazeCell) -> MazeCell:

        row_origin, col_origin = origin.get_position()
        row_target, col_target = target.get_position()

        if row_origin == row_target:
            return self.grid[row_origin][max(col_origin, col_target) - 1]
        else:
            print(row_origin, row_target)
            return self.grid[max(row_origin, row_target) - 1][col_origin]
