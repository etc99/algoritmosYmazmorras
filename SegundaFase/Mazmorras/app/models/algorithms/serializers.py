from pydantic import BaseModel 

class AlgorithmSerializer(BaseModel):
    name: str
    description: str