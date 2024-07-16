from fastapi import APIRouter
from api.v1.home import router as home_router
from api.v1.storages import router as storages_router
from api.v1.products import router as products_router
from api.v1.shelves import router as shelves_router


router = APIRouter(prefix="/v1")
router.include_router(home_router)
router.include_router(storages_router)
router.include_router(products_router)
router.include_router(shelves_router)