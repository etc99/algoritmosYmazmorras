from beanie import Document
from typing import List, Dict, Any
from pydantic import BaseModel



class CompleteDungeon(Document, BaseModel):
    algorithm: str
    seed: int
    parameters: Dict[str, Any]
    maze: List[List[int]]

    def serialize(self):
        return {
            "maze": self.maze
        }