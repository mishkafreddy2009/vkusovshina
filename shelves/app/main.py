from fastapi import Depends, FastAPI
from sqlmodel import Session, select
from sqlmodel.ext.asyncio.session import AsyncSession
from core.db import get_session
from models.shelves import Shelf, ShelfCreate


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/shelves", response_model=list[Shelf])
async def get_shelves(session: AsyncSession=Depends(get_session)):
    result = await session.exec(select(Shelf))
    shelves = result.fetchall()
    return [
        Shelf(
            shelf_type=shelf.shelf_type,
            volume=shelf.volume,
            id=shelf.id,
        )
        for shelf in shelves
    ]


@app.post("/shelves")
async def add_shelf(shelf: ShelfCreate, session: AsyncSession=Depends(get_session)):
    db_shelf = Shelf(shelf_type=shelf.shelf_type, volume=shelf.volume)
    session.add(db_shelf)
    await session.commit()
    await session.refresh(db_shelf)