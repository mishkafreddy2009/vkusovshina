from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.exc import IntegrityError
from models.models import Shelf, ShelfCreate, ShelfPublic, ShelfUpdate
from core.db import get_session
from crud.shelves import crud_shelf


router = APIRouter(prefix="/shelves", tags=["shelves"])


@router.get("/", response_model=list[ShelfPublic])
async def read_shelves(offset: int = 0, limit: int = 100, session: AsyncSession = Depends(get_session)):
    shelves = await crud_shelf.get_multi(session, offset=offset, limit=limit)
    return shelves


@router.post("/", response_model=ShelfPublic)
async def create_shelf(shelf_in: ShelfCreate, session: AsyncSession = Depends(get_session)):
    shelf = await crud_shelf.get(session, name=shelf_in.name)
    if shelf:
        raise HTTPException(
                status_code=409,
                detail="this shelf already exists"
                )
    obj_in = ShelfCreate(
            **shelf_in.model_dump()
            )
    return await crud_shelf.create(session, obj_in)


@router.put("/{shelf_id}/", response_model=ShelfPublic)
async def update_shelf(shelf_id: int, shelf_in: ShelfUpdate, session: AsyncSession = Depends(get_session)):
    shelf = await crud_shelf.get(session, id=shelf_id)
    if not shelf:
        raise HTTPException(
                status_code=404,
                detail="the shelf you are looking for does not exist"
                )
    try:
        shelf = await crud_shelf.update(session, db_obj=shelf, obj_in={
            **shelf_in.model_dump(exclude_none=True),
            })
    except IntegrityError:
        raise HTTPException(
                status_code=409,
                detail="this shelf already exists"
                )
    return shelf