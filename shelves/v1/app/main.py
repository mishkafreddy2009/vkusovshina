from os import getenv
from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI
from sqlmodel import Session, select, create_engine, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from core.db import get_session
from models.shelves import Shelf, ShelfCreate


@asynccontextmanager
async def lifespan(app: FastAPI):
    DATABASE_URL = f"postgresql+asyncpg://postgres:{getenv('postgresql_pass')}@localhost/vkusovshina"
    engine = AsyncEngine(create_engine(DATABASE_URL, echo=True, future=True))
    async with engine.begin() as connection:
        await connection.run_sync(SQLModel.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/shelves", response_model=list[Shelf])
async def get_shelves(session: AsyncSession=Depends(get_session)):
    result = await session.exec(select(Shelf))
    shelves = result.fetchall()
    return [
        Shelf(
            shelf_type=shelf.shelf_type,
            volume=shelf.volume,
            is_full=shelf.is_full,
            id=shelf.id,
        )
        for shelf in shelves
    ]


@app.post("/shelves")
async def add_shelf(shelf: ShelfCreate, session: AsyncSession=Depends(get_session)):
    db_shelf = Shelf(shelf_type=shelf.shelf_type, volume=shelf.volume, is_full=shelf.is_full)
    session.add(db_shelf)
    await session.commit()
    await session.refresh(db_shelf)
    return db_shelf