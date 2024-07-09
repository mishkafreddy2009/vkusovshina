from app.api.models import StorageIn, StorageOut, StorageUpdate
from app.api.db import storages, database


async def add_storage(payload: StorageIn):
    query = storages.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_storages():
    query = storages.select()
    return await database.fetch_all(query=query)


async def get_storage(id):
    query = storages.select(storages.c.id == id)
    return await database.fetch_all(query=query)


async def delete_storage(id):
    query = storages.delete().where(storages.c.id == id)
    return await database.execute(query=query)


async def update_storage(id: int, payload: StorageIn):
    query = storages.update().where(storages.c.id == id).values(**payload.dict())
    return await database.execute(query=query)
