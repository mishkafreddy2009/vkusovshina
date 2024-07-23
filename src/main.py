from fastapi import FastAPI
from contextlib import asynccontextmanager

from fastapi_users import FastAPIUsers

from auth.auth import auth_backend
from auth.manager import get_user_manager
from database import User
from router import product_router, basket_router, purchase_router, customer_router
from schemas import UserRead, UserCreate


# Контекстный менеджер для управления жизненным циклом приложения
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("включение")
    yield
    print("Выключение")


# fastapi_user + роутеры
app = FastAPI(lifespan=lifespan)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Покупатель"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Покупатель"],
)
app.include_router(product_router)
app.include_router(basket_router)
app.include_router(purchase_router)
app.include_router(customer_router)

