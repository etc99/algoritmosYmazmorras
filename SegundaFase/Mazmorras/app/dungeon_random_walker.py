from typing import *
from .dungeon_base import MazeCell
from .dungeon_base import *
import random


class DungeonRandomWalker(DungeonBase):

    def __init__(self, width: int, height: int, number_of_paths: int = None) -> None:
        super().__init__(width, height)

        self.number_of_paths: int = (
            (width * height) // 1.5) if not number_of_paths else number_of_paths
        self._create_dungeon()

    def _create_dungeon(self) -> None:
        movements: List[Tuple[int, int]] = [
            (1, 0),
            (-1, 0),
            (0, -1),
            (0, 1)
        ]

        current_position: CellPosition = (random.randint(
            0, self.height - 1), random.randint(0, self.width - 1))

        self.start_cell: MazeCell = self.get_cell(current_position)
        position_set: Set[CellPosition] = {current_position}

        while len(position_set) < self.number_of_paths:
            movement: CellPosition = random.choice(movements)

            test_position: CellPosition = (
                current_position[0] + movement[0], current_position[1] + movement[1])

            if not self.inside_map(test_position):
                continue
            current_position = test_position
            position_set.add(current_position)

        self.exit_cell: MazeCell = self.get_cell(current_position)

        for position in position_set:
            self.get_cell(position).change_state(CellType.PATH)

        self.exit_cell.change_state(CellType.EXIT)
        self.start_cell.change_state(CellType.START)
