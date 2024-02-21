from sqlalchemy.orm import Session
from app.models.algorithms.schemas import Algorithm
from app.models.algorithms.serializers import AlgorithmSerializer

def listAlgorithms(db:Session, skip: int=0, limit: int=100):
    return db.query(Algorithm).offset(skip).limit(limit).all()