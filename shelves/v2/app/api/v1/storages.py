from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.exc import IntegrityError
from models.models import Storage, StorageCreate, StoragePublic, StorageUpdate
from core.db import get_session
from crud.storages import crud_storage


router = APIRouter(prefix="/storages", tags=["storages"])


@router.get("/", response_model=list[StoragePublic])
async def read_storages(offset: int = 0, limit: int = 100, session: AsyncSession = Depends(get_session)):
    storages = await crud_storage.get_multi(session, offset=offset, limit=limit)
    return storages


@router.post("/", response_model=StoragePublic)
async def create_storage(storage_in: StorageCreate, session: AsyncSession = Depends(get_session)):
    storage = await crud_storage.get(session, name=storage_in.name)
    if storage:
        raise HTTPException(
                status_code=409,
                detail="this storage already exist"
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
                detail="this storage doesnt exist"
                )
    try:
        storage = await crud_storage.update(session, db_obj=storage, obj_in={
            **storage_in.model_dump(exclude_none=True),
            })
    except IntegrityError:
        raise HTTPException(
                status_code=409,
                detail="this storage already exist"
                )
    return storage
