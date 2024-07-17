from fastapi import APIRouter

from app.api.v1.storages import router as storages_router
from app.api.v1.products import router as products_router

router = APIRouter(prefix="/v1")
router.include_router(storages_router)
router.include_router(products_router)
