from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.exc import IntegrityError
from models.models import Product, ProductCreate, ProductPublic, ProductUpdate
from core.db import get_session
from crud.products import crud_product


router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=list[ProductPublic])
async def read_products(offset: int = 0, limit: int = 100, session: AsyncSession = Depends(get_session)):
    products = await crud_product.get_multi(session, offset=offset, limit=limit)
    return products


@router.post("/", response_model=ProductPublic)
async def create_product(product_in: ProductCreate, session: AsyncSession = Depends(get_session)):
    product = await crud_product.get(session, title=product_in.title)
    if product:
        raise HTTPException(
                status_code=409,
                detail="this product already exist"
                )
    obj_in = ProductCreate(
            **product_in.model_dump()
            )
    return await crud_product.create(session, obj_in)


@router.put("/{product_id}/", response_model=ProductPublic)
async def update_product(product_id: int, product_in: ProductUpdate, session: AsyncSession = Depends(get_session)):
    product = await crud_product.get(session, id=product_id)
    if not product:
        raise HTTPException(
                status_code=404,
                detail="the product you are looking for does not exist"
                )
    try:
        product = await crud_product.update(session, db_obj=product, obj_in={
            **product_in.model_dump(exclude_none=True),
            })
    except IntegrityError:
        raise HTTPException(
                status_code=409,
                detail="this product already exist"
                )
    return product