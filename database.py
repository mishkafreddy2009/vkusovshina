from datetime import date

from sqlalchemy import Column, PickleType
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# Создание асинхронного движка для работы с SQLite
engine = create_async_engine("sqlite+aiosqlite:///tasks.db")
# Создание фабрики сессий для работы с базой данных
new_session = async_sessionmaker(engine, expire_on_commit=False)


# Базовая модель для всех таблиц
class Model(DeclarativeBase):
    pass


class ProductTable(Model):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[int]
    quantity: Mapped[int]
    price: Mapped[float]


class BasketTable(Model):
    __tablename__ = "baskets"

    id: Mapped[int] = mapped_column(primary_key=True)
    pr_category: Mapped[str]
    cust_id: Mapped[int]
    pr_price: Mapped[float]
    quantity: Mapped[int]


class PurchaseTable(Model):
    __tablename__ = "purchases"

    id: Mapped[int] = mapped_column(primary_key=True)
    cust_id: Mapped[int]
    time: Mapped[date]
    total_cost: Mapped[float]
    pr_list: Mapped[PickleType] = Column(PickleType)


# Асинхронная функция для создания всех таблиц
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


# Асинхронная функция для удаления всех таблиц
async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
