from fastapi import APIRouter
from app.models.algorithms.api import router as algorithms_router

router = APIRouter()
router.include_router(algorithms_router, prefix='/algorithms')