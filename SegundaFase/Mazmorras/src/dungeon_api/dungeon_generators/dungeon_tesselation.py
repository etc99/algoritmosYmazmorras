from .dungeon_base import *
import random
import copy


class DungeonTesselation(DungeonBase):

    def __init__(self, iters: int = 10, seed: int | None = None) -> None:

        self.max_iters: int = iters
        self.seed: int = int(seed) if seed else random.randint(0,1000)

        self.grid: List[List[MazeCell]] = [
            [MazeCell(0, 0), MazeCell(0, 0), MazeCell(0, 0)],
            [MazeCell(0, 0), MazeCell(
                0, 0, state=CellType.PATH), MazeCell(0, 0)],
            [MazeCell(0, 0), MazeCell(0, 0), MazeCell(0, 0)],
        ]

        self._create_dungeon()

    def _create_dungeon(self) -> None:
        for _ in range(self.max_iters):
            self.tesselation()

    def check_vertical_apperture(self, y: int, x: int) -> bool:
        if y - 1 < 0 or y + 1 > len(self.grid) - 1:
            return False
        return self.grid[y + 1][x].state == CellType.PATH and self.grid[y-1][x].state == CellType.PATH

    def check_horizontal_apperture(self, y: int, x: int) -> bool:
        if x - 1 < 0 or x + 1 > len(self.grid[0]) - 1:
            return False

        return self.grid[y][x + 1].state == CellType.PATH and self.grid[y][x - 1].state == CellType.PATH

    def tesselation(self) -> None:
        pre_size_x: int = len(self.grid[0]) - 1
        pre_size_y: int = len(self.grid) - 1

        for row in self.grid[:]:
            row.extend(copy.deepcopy(row[1:]))
        for row in self.grid[1:]:
            self.grid.append(copy.deepcopy(row[:]))

        appertures: List[CellPosition] = []
        appertures.append(random.choice([(i, pre_size_x) for i in range(
            pre_size_y + 1) if self.check_horizontal_apperture(i, pre_size_x)]))
        appertures.append(random.choice([(i, pre_size_x) for i in range(
            pre_size_y, len(self.grid)) if self.check_horizontal_apperture(i, pre_size_x)]))
        appertures.append(random.choice([(pre_size_y, i) for i in range(
            pre_size_x + 1) if self.check_vertical_apperture(pre_size_y, i)]))
        appertures.append(random.choice([(pre_size_y, i) for i in range(
            pre_size_x, len(self.grid)) if self.check_vertical_apperture(pre_size_y, i)]))

        random.shuffle(appertures)
        appertures.pop()

        for app in appertures:
            self.grid[app[0]][app[1]].change_state(CellType.PATH)
