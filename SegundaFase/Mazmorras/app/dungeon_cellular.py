from typing import *
from typing import List
import copy

from .dungeon_base import MazeCell
from .dungeon_base import DungeonBase, CellPosition, CellType, MazeCell
import random


class DungeonCellular(DungeonBase):

    def __init__(self,
                 width: int,
                 height: int,
                 max_iterations: int = 10000,
                 starting_points: List[CellPosition] = []) -> None:
        self.width: int = width
        self.height: int = height

        maze_list: List[List[MazeCell]] = []

        for i in range(self.height):
            new_row: List[MazeCell] = []
            for j in range(self.width):
                new_row.append(MazeCell(i, j, state=CellType.PATH))
            maze_list.append(new_row)
        self.grid: List[List[MazeCell]] = maze_list
        self.iters: int = max_iterations
        if not starting_points:
            starting_points_set: Set[CellPosition] = set()
            num_starting: int = (self.width * self.height) // 2
            while len(starting_points_set) < num_starting:
                starting_points_set.add(
                    (random.randint(0, self.height - 1), random.randint(0, self.width - 1)))

            starting_points = list(starting_points_set)

        for point in starting_points:
            self.get_cell(point).change_state(CellType.WALL)

        self._create_dungeon()

    def get_neighbors(self, cell: MazeCell, distance: int = 1) -> List[MazeCell]:

        directions: List[Tuple[int, int]] = [
            (-distance, -distance), (0, -distance), (distance, -distance),
            (distance, -distance), (distance, 0), (distance, distance),
            (-distance, 0), (0, distance)
        ]

        position: CellPosition = cell.get_position()

        neighbors: List[MazeCell] = []
        for direction in directions:
            check_position: CellPosition = (
                position[0] + direction[0], position[1] + direction[1])

            if not self.inside_map(check_position):
                continue

            neighbors.append(self.get_cell(check_position))

        return neighbors

    def _create_dungeon(self) -> None:

        for _ in range(self.iters):
            self.__generation()

        
    def __generation(self) -> None:

        new_grid: List[List[MazeCell]] = copy.deepcopy(self.grid)

        for row in self.grid:
            for cell in row:
                pos_y, pos_x = cell.get_position()
                num_neigh: int = sum(
                    1 for cell in self.get_neighbors(cell) if cell.state == CellType.WALL)

                if num_neigh > 4 or num_neigh < 1:
                        new_grid[pos_y][pos_x].change_state(CellType.PATH)
                elif num_neigh == 3:        
                        new_grid[pos_y][pos_x].change_state(CellType.WALL)

        self.grid = new_grid
