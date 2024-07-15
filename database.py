from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import date


engine = create_async_engine(
    "sqlite+aiosqlite:///supplies.db"
)
new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class Supplies(Model):
    __tablename__ = "supplies"

    id: Mapped[int] = mapped_column(primary_key=True)
    provider_id: Mapped[int]
    store_id: Mapped[int]
    date: Mapped[date]


class DeliveredProducts(Model):
    __tablename__ = "delivered_products"

    id: Mapped[int] = mapped_column(primary_key=True)
    supplies_id: Mapped[int]
    amount: Mapped[int]


class Provider(Model):
    __tablename__ = "provider"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    contacts: Mapped[str | None]


class Store(Model):
    __tablename__ = "store"

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str]


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)

