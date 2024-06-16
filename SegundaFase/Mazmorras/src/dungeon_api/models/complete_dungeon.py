from beanie import Document
from typing import List, Dict, Any
from pydantic import BaseModel



class DungeonResponse(Document, BaseModel):
    algorithm: str
    seed: int
    parameters: Dict[str, Any]
    maze: List[List[int]]