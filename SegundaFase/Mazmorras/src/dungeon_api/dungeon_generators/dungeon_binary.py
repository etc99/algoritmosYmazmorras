from .dungeon_base import *
from typing import List
import random

class DungeonBinaryTree(SizeableDungeon):

    def __init__(self, width: int, height: int, seed: int | None = None) -> None:
        super().__init__(width, height, seed)

    def _create_dungeon(self) -> None:

        for row in range(1, self.height, 2):
            for column in range(1, self.width, 2):
                cell: MazeCell = self.get_cell((row, column))
                upper_cell: MazeCell | None = self.get_upper_cell(cell)
                right_cell: MazeCell | None = self.get_right_cell(cell)

                if not upper_cell and not right_cell:
                    continue

                if not upper_cell:
                    self.connect_cells(cell, right_cell)
                elif not right_cell:
                    self.connect_cells(cell, upper_cell)
                else:
                    self.connect_cells(cell, random.choice((upper_cell, right_cell)))

    def get_upper_cell(self, cell: MazeCell) -> MazeCell | None:

        if self.inside_map((cell.row + 2, cell.column)):
            return self.get_cell((cell.row + 2, cell.column))
        return None

    def get_right_cell(self, cell: MazeCell) -> MazeCell | None:
        if self.inside_map((cell.row, cell.column + 2)):
            return self.get_cell((cell.row, cell.column + 2))
        return None

    def connect_cells(self, origin: MazeCell, target: MazeCell) -> None:
        origin_row, origin_col = origin.get_position()
        target_row, target_col = target.get_position()

        row_distance: int = abs(origin_row - target_row)
        col_distance: int = abs(origin_col - target_col)
        passage: MazeCell
        if row_distance != 0:
            passage = self.get_cell((min(
            origin_row, target_row) + 1, target_col))
        else:
            passage = self.get_cell(( target_row + row_distance, min(origin_col, target_col) + 1))
        origin.change_state(CellType.PATH)
        target.change_state(CellType.PATH)
        passage.change_state(CellType.PATH)
