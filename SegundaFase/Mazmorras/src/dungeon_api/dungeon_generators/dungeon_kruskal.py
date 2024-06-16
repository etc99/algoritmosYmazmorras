from .dungeon_base import *
import random

from itertools import product


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
        edges: List[Tuple[MazeCell, MazeCell]] = []
        for row, column in product(range(1,self.height, 2), range(1,self.width, 2)):
            flattened_maze.append(self.get_cell((row,column)))

        for row in range(1, self.height - 1 , 2):
            for column in range(1, self.width - 1, 2):
                edges.append((self.get_cell((row,column)), self.get_cell((row + 2,column))))
                edges.append((self.get_cell((row,column)), self.get_cell((row ,column + 2))))

        for column in range(1, self.width - 1 , 2):
            edges.append((self.get_cell(( self.height - 1, column)), self.get_cell(( self.height - 1,  column +2 ))))


        union_find: UnionFind = UnionFind(flattened_maze)
        random.shuffle(edges)

        while edges:
            A,B = edges.pop()

            if union_find.find(A) == union_find.find(B):
                continue

            self.get_cell_between(A,B).change_state(CellType.PATH)
            A.change_state(CellType.PATH)
            B.change_state(CellType.PATH)
            union_find.union(A,B)


    
    def get_cell_between(self, origin: MazeCell, target: MazeCell) -> MazeCell:

        row_origin, col_origin = origin.get_position()
        row_target, col_target = target.get_position()

        if row_origin == row_target:
            return self.grid[row_origin][max(col_origin, col_target) - 1]
        else:
            return self.grid[max(row_origin, row_target) - 1][col_origin]
        