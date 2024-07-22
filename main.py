from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager

from fastapi_users import FastAPIUsers

from auth.auth import auth_backend
from auth.manager import get_user_manager
#from database import create_tables, delete_tables, User
from database import User
#from database import create_tables
from router import product_router, basket_router, purchase_router
from schemas import UserRead, UserCreate


# Контекстный менеджер для управления жизненным циклом приложения
@asynccontextmanager
async def lifespan(app: FastAPI):
    # # Удаление всех таблиц перед запуском
    # await delete_tables()
    # print("База очищена")
    # Создание всех таблиц перед запуском
    # await create_tables()
    # print("База готова к работе")
    print("включение")
    yield
    # Действия при завершении работы приложения
    print("Выключение")


#добавляем пользователя


# Создание экземпляра приложения FastAPI с управлением жизненным циклом
app = FastAPI(lifespan=lifespan)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(product_router)
app.include_router(basket_router)
app.include_router(purchase_router)
