from fastapi import APIRouter, File, status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import UploadFile
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.models.product import Product
from app.models.product import ProductCreate
from app.models.product import ProductPublic
from app.models.product import ProductUpdate
from app.core.db import get_session
from app.crud.products import crud_product

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


# @router.post("/uploadfile/{product_id}")
# async def upload_product_image(product_in: ProductCreate, product_id: int,session: AsyncSession = Depends(get_session), file: UploadFile = File(...)):
#     FILEPATH = "./static/images"
#     file_name = file.filename
#
#     try:
#         extension = file_name.split(".")[1]
#     finally:
#         if extension not in ["png", "jpg", "jpeg"]:
#             raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
#                                 detail="File extension not allowed")
#
#     token_name = "product" + "safsafsaf" + "." + extension
#     generated_name = FILEPATH + token_name
#     file_content = await file.read()
#
#     with open(generated_name, "wb") as f:
#         f.write(file_content)
#
#     product = await crud_product.get(session, title=product_in.title)
#     if not product:
#         raise HTTPException(
#                 status_code=404,
#                 detail="this product already exist"
#                 )


@router.put("/{product_id}/", response_model=ProductPublic)
async def update_product(storage_id: int, storage_in: ProductUpdate, session: AsyncSession = Depends(get_session)):
    storage = await crud_product.get(session, id=storage_id)
    if not storage:
        raise HTTPException(
                status_code=404,
                detail="this storage doesnt exist"
                )
    try:
        storage = await crud_product.update(session, db_obj=storage, obj_in={
            **storage_in.model_dump(exclude_none=True),
            })
    except IntegrityError:
        raise HTTPException(
                status_code=409,
                detail="this storage already exist"
                )
    return storage
