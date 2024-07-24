from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from core.db import get_session

from sqlmodel.ext.asyncio.session import AsyncSession
from models.models import Storage, Shelf, Product


async def attach_products_to_shelf(
    session: AsyncSession, storage_id: int, shelf_id: int, product_ids: list[int]
):
    async with session() as sess:
        storage = await sess.get(Storage, storage_id)
        if not storage:
            raise HTTPException(status_code=404, detail="Storage not found")
        
        shelf = await sess.get(Shelf, shelf_id)
        if not shelf:
            raise HTTPException(status_code=404, detail="Shelf not found")
        
        products = await sess.get_multi(Product, ids=product_ids)
        if len(products) != len(product_ids):
            raise HTTPException(status_code=404, detail="One or more products not found")

        shelf.products.extend(products)
        await sess.commit()
        await sess.refresh(shelf)
        return shelf

async def detach_products_from_shelf(
    session: AsyncSession, storage_id: int, shelf_id: int, product_ids: list[int]
):
    async with session() as sess:
        storage = await sess.get(Storage, storage_id)
        if not storage:
            raise HTTPException(status_code=404, detail="Storage not found")
        
        shelf = await sess.get(Shelf, shelf_id)
        if not shelf:
            raise HTTPException(status_code=404, detail="Shelf not found")
        
        products = await sess.get_multi(Product, ids=product_ids)
        if len(products) != len(product_ids):
            raise HTTPException(status_code=404, detail="One or more products not found")

        for product in products:
            if product in shelf.products:
                shelf.products.remove(product)
        
        await sess.commit()
        await sess.refresh(shelf)
        return shelf
