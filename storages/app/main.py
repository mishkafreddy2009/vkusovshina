from fastapi import Depends, FastAPI
from sqlmodel import Session, select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.db import get_session
from app.models.storages import Storage, StorageCreate

# from app.api import router
# from app.core.config import settings

app = FastAPI()


@app.get("/ping")
async def pong():
    return {"ping": "pong"}


@app.get("/storages", response_model=list[Storage])
async def get_storages(session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Storage))
    storages = result.fetchall()
    return [
        Storage(
            name=storage.name,
            address=storage.address,
            phone_number=storage.phone_number,
            id=storage.id,
        )
        for storage in storages
    ]


@app.post("/storages")
async def add_storage(
    storage: StorageCreate,
    session: AsyncSession = Depends(get_session)
):
    db_storage = Storage(
        name=storage.name, address=storage.address, phone_number=storage.phone_number
    )
    session.add(db_storage)
    await session.commit()
    await session.refresh(db_storage)
    return storage
