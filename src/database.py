import os
from datetime import date, datetime
from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase, SQLAlchemyBaseUserTable
from sqlalchemy import Column, PickleType, Integer, String, TIMESTAMP, ForeignKey, Boolean, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncEngine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config import DB_USER, DB_HOST, DB_PORT, DB_PASS, DB_NAME
from models import role

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
#
#     DB_HOST="localhost",
#     DB_PORT = "5433",
#     DB_USER="postgres",
#     DB_PASSWORD="1234",
#     DB_NAME="mydatabase"
#
engine = AsyncEngine(create_engine(DATABASE_URL, echo=True, future=True))

# Создание фабрики сессий для работы с базой данных
new_session = async_sessionmaker(engine, expire_on_commit=False)


# Базовая модель для всех таблиц
class Model(DeclarativeBase):
    pass


class ProductTable(Model):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str]
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


#добавляем пользователя

class User(SQLAlchemyBaseUserTable[int], Model):
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey(role.c.id))
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with new_session() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)

