from .dungeon_base import *
from typing import Dict, Set


class DungeonEller(SizeableDungeon):

    def __init__(self, width: int, height: int, seed: int | None = None) -> None:
        self.set_index: int = 0
        self.cell_set: Dict[MazeCell, Set[MazeCell]] = dict()
        super().__init__(width, height, seed)

    def _create_dungeon(self) -> None:

        set_index: int = 0
        for row_index in range(1, self.height - 2, 2):
            row: List[MazeCell] = self.get_row(row_index)

            self.create_sets(row)

            self.group_adyacent(row)

            next_row: List[MazeCell] = self.get_row(row_index + 2)

            self.create_sets(next_row)
            n_vertical_connections: int = random.randint(1, self.width // 2 - 1)

            self.create_vertical_connections( n_vertical_connections, row, next_row)

        last_row: List[MazeCell] = self.get_row(self.height - 1 if self.height % 2 != 0 else self.height - 1)
        self.create_sets(last_row)
        self.group_adyacent(last_row)


    def create_sets(self, row: List[MazeCell]):

        for cell in row:

            if cell not in self.cell_set:
                self.cell_set[cell] = {cell}



    def create_vertical_connections(self, number: int, row: List[MazeCell], next_row: List[MazeCell]) -> None:

        possible_connections: List[Tuple[MazeCell, MazeCell]] = [
            (cell_a, cell_b) for cell_a, cell_b in zip(row, next_row)]

        random.shuffle(possible_connections)

        for _ in range(number):
            a, b = possible_connections.pop()

            self.join_sets(a,b)
            self.connect_cells(a, b)

    def group_adyacent(self, row: List[MazeCell]) -> None:
        pairs: List[Tuple[MazeCell, MazeCell]] = [
            (cell_a, cell_b) for cell_a, cell_b in zip(row[:-1], row[1:])]

        random.shuffle(pairs)

        for pair in pairs:
            a, b = pair

            if self.cell_set[a] == self.cell_set[b]:
                continue

            self.join_sets(a,b)
            self.connect_cells(a, b)


    def join_sets(self, cell_a: MazeCell, cell_b: MazeCell) -> None:
            previous_state_a = self.cell_set[cell_a].copy()
            previous_state_b = self.cell_set[cell_b].copy()

            new_set = previous_state_a.union(previous_state_b)

            for cell in [*previous_state_a, *previous_state_b]:
                self.cell_set[cell] = new_set

    def get_row(self, index: int) -> List[MazeCell]:
        return self.grid[index][1:self.width:2]

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
        target.change_state(CellType.PATH)
        passage.change_state(CellType.PATH)
