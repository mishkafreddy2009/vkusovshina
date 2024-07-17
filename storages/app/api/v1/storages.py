from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.models.storage import StorageCreate
from app.models.storage import StoragePublic
from app.models.storage import StorageUpdate
from app.core.db import get_session
from app.crud.storages import crud_storage

router = APIRouter(prefix="/storages", tags=["storages"])


@router.get("/", response_model=list[StoragePublic])
async def read_storages(offset: int = 0, limit: int = 100, session: AsyncSession = Depends(get_session)):
    storages = await crud_storage.get_multi(session, offset=offset, limit=limit)
    return storages


@router.get("/{storage_id}/", response_model=StoragePublic)
async def read_storage(storage_id: int, session: AsyncSession = Depends(get_session)):
    storage = await crud_storage.get(session, id=storage_id)
    if not storage:
        raise HTTPException(
                status_code=404,
                detail="storage not found"
                )
    return storage


@router.post("/", response_model=StoragePublic)
async def create_storage(storage_in: StorageCreate, session: AsyncSession = Depends(get_session)):
    storage = await crud_storage.get(session, title=storage_in.title)
    if storage:
        raise HTTPException(
                status_code=409,
                detail="storage already exist"
                )
    obj_in = StorageCreate(
            **storage_in.model_dump()
            )
    return await crud_storage.create(session, obj_in)


@router.put("/{storage_id}/", response_model=StoragePublic)
async def update_storage(storage_id: int, storage_in: StorageUpdate, session: AsyncSession = Depends(get_session)):
    storage = await crud_storage.get(session, id=storage_id)
    if not storage:
        raise HTTPException(
                status_code=404,
                detail="storage not found"
                )
    try:
        storage = await crud_storage.update(session, db_obj=storage, obj_in={
            **storage_in.model_dump(exclude_none=True),
            })
    except IntegrityError:
        raise HTTPException(
                status_code=409,
                detail="storage already exist"
                )
    return storage
