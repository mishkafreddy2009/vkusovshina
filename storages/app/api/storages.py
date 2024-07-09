from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from app.api.models import Storage, StorageOut, StorageIn
from app.api import db_manager

storages = APIRouter()


@storages.get("/", response_model=list[StorageOut])
async def index():
    return await db_manager.get_all_storages()


@storages.post("/", status_code=201)
async def add_storage(payload: StorageIn):
    storage_id = await db_manager.add_storage(payload)
    response = {"id": storage_id, **payload.dict()}
    return response


@storages.put("/{id}")
async def update_storage(id: int, payload: Storage):
    storage = await db_manager.get_storage(id)
    if not storage:
        raise HTTPException(status_code=404, detail="storage not found")

    update_data = payload.dict(exclude_unset=True)
    storage_in_db = StorageIn(**storage)

    updated_storage = storage_in_db.copy(update=update_data)

    return await db_manager.update_storage(id, updated_storage)


@storages.delete("/{id}")
async def delete_storage(id: int):
    storage = await db_manager.get_storage(id)
    if not storage:
        raise HTTPException(status_code=404, detail="storage not found")
    return await db_manager.delete_storage(id)
