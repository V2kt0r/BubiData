from fastapi import APIRouter

from .distance import router as distance_router
from .history import router as history_router

router = APIRouter(prefix="/api")

router.include_router(history_router)
router.include_router(distance_router)
