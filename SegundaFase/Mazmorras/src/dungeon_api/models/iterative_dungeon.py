from beanie import Document
from typing import List, Tuple, Dict, Any
from pydantic import BaseModel

class IterativeDungeon(Document, BaseModel):
    algorithm: str
    seed: int
    parameters: Dict[str, Any]
    steps: List[Tuple[int, int]]