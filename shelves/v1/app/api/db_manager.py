from api.models import ShelfIn, ShelfOut, ShelfUpdate
from api.db import shelves, database


async def add_shelf(payload: ShelfIn):
    query = shelves.insert().values(**payload.model_dump())
    return await database.execute(query=query)


async def get_all_shelves():
    query = shelves.select()
    return await database.fetch_all(query=query)


async def get_shelf(id: int):
    query = shelves.select(shelves.c.id == id)
    return await database.fetch_all(query=query)


async def delete_shelf(id: int):
    query = shelves.delete().where(shelves.c.id == id)
    return await database.execute(query=query)


async def update_shelf(id: int, payload: ShelfIn):
    query = shelves.update().where(shelves.c.id == id).values(**payload.model_dump())
