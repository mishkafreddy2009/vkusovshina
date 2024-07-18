from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from repository import ProductRepository, BasketRepository, PurchaseRepository
from schemas import SProductAdd, SProductId, SProduct, SBasketAdd, SBasketId, SBasket, \
    SPurchase, SPurchaseId

# Новый роутер для продуктов
product_router = APIRouter(
    prefix="/products",
    tags=["Продукты"],
)


@product_router.post("")
async def add_product(
        product: Annotated[SProductAdd, Depends()],
) -> SProductId:
    product_id = await ProductRepository.add_one(product)
    return {"ok": True, "product_id": product_id}


@product_router.get("")
async def get_products() -> list[SProduct]:
    products = await ProductRepository.find_all()
    return products


# Новый роутер для корзины
basket_router = APIRouter(
    prefix="/baskets",
    tags=["Корзина"],
)


@basket_router.post("")
async def add_to_basket(
        basket: Annotated[SBasketAdd, Depends()],
) -> SBasketId:
    basket_id = await BasketRepository.add_one(basket)
    return {"ok": True, "basket_id": basket_id}


@basket_router.get("")
async def get_basket() -> list[SBasket]:
    baskets = await BasketRepository.find_all()
    return baskets


purchase_router = APIRouter(
    prefix="/purchases",
    tags=["Покупки"],
)


@purchase_router.post("")
async def complete_purchase():
    purchase_id = await PurchaseRepository.complete_purchase()
    return {"purchase_id": purchase_id}


@purchase_router.get("/123")
async def get_purchases():
    purchases = await PurchaseRepository.find_all()
    return {"purchases": purchases}
