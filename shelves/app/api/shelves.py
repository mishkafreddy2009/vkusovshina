from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from models import Shelf, ShelfIn, ShelfOut
import db_manager


shelves = APIRouter()


@shelves.get("/", response_model=list[ShelfOut])
async def index():
    return await db_manager.get_all_shelves()


@shelves.post("/", status_code=201)
async def add_shelf(payload: ShelfIn):
    shelf_id = await db_manager.add_shelf(payload)
    response = {"id": shelf_id, **payload.model_dump()}
    return response


@shelves.put("/{id}")
async def update_shelf(id: int, payload: Shelf):
    shelf = await db_manager.get_shelf(id)
    if not shelf:
        raise HTTPException(status_code=404, detail="shelf not found")
    
    update_data = payload.model_dump(exclude_unset=True)
    shelf_in_db = ShelfIn(**shelf)

    updated_shelf = shelf_in_db.model_copy(update=update_data)

    return await db_manager.update_shelf(id, updated_shelf)


@shelves.delete("/{id}")
async def delete_shelf(id: int):
    shelf = await db_manager.get_shelf(id)
    if not shelf:
        raise HTTPException(status_code=404, detail="shelf not found")
    return await db_manager.delete_shelf(id)
