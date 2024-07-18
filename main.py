from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import product_router, basket_router, purchase_router


# Контекстный менеджер для управления жизненным циклом приложения
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Удаление всех таблиц перед запуском
    await delete_tables()
    print("База очищена")
    # Создание всех таблиц перед запуском
    await create_tables()
    print("База готова к работе")
    yield
    # Действия при завершении работы приложения
    print("Выключение")


# Создание экземпляра приложения FastAPI с управлением жизненным циклом
app = FastAPI(lifespan=lifespan)

app.include_router(product_router)
app.include_router(basket_router)
app.include_router(purchase_router)