from typing import Annotated, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, FastAPI
from fastapi_users import FastAPIUsers

from auth.auth import auth_backend
from auth.manager import get_user_manager
from database import User
from repository import ProductRepository, BasketRepository, PurchaseRepository, UserRepository
from schemas import SProductAdd, SProductId, SProduct, SBasketAdd, SBasketId, SBasket, \
    SPurchase, SPurchaseId, UserRead, UserCreate

# Новый роутер для продуктов
product_router = APIRouter(
    prefix="/products",
    tags=["Продукты"],
)

#для юзера
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()
#

@product_router.post("")
async def add_product(
        product: Annotated[SProductAdd, Depends()],
) -> dict[str, str | int]:
    product_id = await ProductRepository.add_one(product)
    pr_cat = product.category
    count_pr = product.quantity
    return {"Добавлен товар": pr_cat, "В количестве": count_pr, "product_id": product_id}


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
        user: User = Depends(current_user),
) -> dict[str, int | Any]:
    basket_id = await BasketRepository.add_one(basket, user)
    pr_cat = basket.pr_category
    count_pr = basket.quantity
    return {"Добавлен товар": pr_cat, "В количестве": count_pr, "basket_id": basket_id, "you": user.username}


@basket_router.get("")
async def get_basket() -> list[SBasket]:
    baskets = await BasketRepository.find_all()
    return baskets


purchase_router = APIRouter(
    prefix="/purchases",
    tags=["Покупки"],
)


@purchase_router.post("")
async def complete_purchase(user: User = Depends(current_user)):
    purchase_id = await PurchaseRepository.complete_purchase()
    return {"Покупка совершена purchase_id": purchase_id, "you": user.username}


@purchase_router.get("/123")
async def get_purchases():
    purchases = await PurchaseRepository.find_all()
    return {"purchases": purchases}


@purchase_router.get("/12345")
async def get_users():
    users = await UserRepository.find_all()
    return {"purchases": users}
