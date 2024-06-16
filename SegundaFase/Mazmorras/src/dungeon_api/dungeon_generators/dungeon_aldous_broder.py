from .dungeon_base import *
import random


class DungeonAldousBroder(SizeableDungeon):


    def __init__(self, width: int, height: int, seed: int | None = None) -> None:
        super().__init__(width, height, seed)

    def _create_dungeon(self) -> None:

        unvisited_cells: List[MazeCell] = [cell for row in self.grid[:self.height:2] for cell in row[:self.width:2] ]

        current_cell: MazeCell = random.choice([cell for row in self.grid[:self.height:2] for cell in row[:self.width:2] ])
        
        remaining_cells: int = len(unvisited_cells)

        while remaining_cells:
            if current_cell.state == CellType.WALL:
                current_cell.state = CellType.PATH
                remaining_cells -= 1
            new_cell: MazeCell = random.choice(self.get_neighbors(current_cell, distance=2))
            if new_cell.state == CellType.WALL:
                self.connect_cells(current_cell, new_cell)
            current_cell = new_cell



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
            passage = self.get_cell(
                (target_row + row_distance, min(origin_col, target_col) + 1))
        origin.change_state(CellType.PATH)
        # target.change_state(CellType.PATH)
        passage.change_state(CellType.PATH)
