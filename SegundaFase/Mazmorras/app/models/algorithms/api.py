from fastapi import APIRouter
from app.models.algorithms.orm import listAlgorithms
from app.models.algorithms.serializers import AlgorithmSerializer
from fastapi import Depends
from app.dependencies import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get('/', response_model=list[AlgorithmSerializer])
def list_algorithms(skip: int=0, limit:int =100, db: Session=Depends(get_db)):
    items = listAlgorithms(db, skip, limit)
    return items