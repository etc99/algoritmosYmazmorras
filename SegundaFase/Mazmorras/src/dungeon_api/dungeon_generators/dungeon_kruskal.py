from dungeon_base import *
import random


class UnionFind:

    def __init__(self, objs: List[MazeCell]) -> None:
        
        self.parents: Dict[MazeCell, int] = {}
        self.sets: Dict[int, Set[MazeCell]] = {}

        for i, obj in enumerate(objs):
            self.parents[obj] = i
            self.sets[i] = {obj}


    def find(self, obj: MazeCell) -> int:
        return self.parents[obj] 
    

    def union(self, obj1: MazeCell, obj2: MazeCell) -> None:
        p1: int = self.find(obj1)
        p2: int = self.find(obj2)

        for obj in self.sets[p1]:
            self.parents[obj] = p2
            self.sets[p2].add(obj)


    def __str__(self) -> str:
        return f"parents: {self.parents} sets: {self.sets}"




class DungeonKruskal(SizeableDungeon):

    def __init__(self, width: int, height: int, seed: int | None = None, **kwargs) -> None:
        super().__init__(width, height, seed, **kwargs)

    def _create_dungeon(self) -> None:
        flattened_maze: List[MazeCell] = []
        for cells in self.grid:
            flattened_maze.extend(cells)

        union_find: UnionFind = UnionFind(flattened_maze)
        random.shuffle(flattened_maze)

        while flattened_maze:

            cell: MazeCell = flattened_maze.pop()


            neighs: List[MazeCell] = self.get_neighbors(cell, distance=2)

            connect: MazeCell = random.choice(neighs)

            if union_find.find(cell) != union_find.find(connect):
                passage: MazeCell = self.get_cell_between(cell, connect)

                if passage.state == CellType.PATH:
                    continue
                union_find.union(passage,cell)
                union_find.union(cell, connect )
                passage.change_state(CellType.PATH)
                cell.change_state(CellType.PATH)
                connect.change_state(CellType.PATH)
                if passage in flattened_maze:
                    flattened_maze.remove(passage)
                if connect in flattened_maze:
                    flattened_maze.remove(connect)




    
    def get_cell_between(self, origin: MazeCell, target: MazeCell) -> MazeCell:

        row_origin, col_origin = origin.get_position()
        row_target, col_target = target.get_position()

        if row_origin == row_target:
            return self.grid[row_origin][max(col_origin, col_target) - 1]
        else:
            return self.grid[max(row_origin, row_target) - 1][col_origin]