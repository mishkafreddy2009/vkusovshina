from fastapi import APIRouter

router = APIRouter(prefix="/home", tags=["home"])


@router.get("/")
async def home():
    return "hello workd"
