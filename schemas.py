from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict



class SProductAdd(BaseModel):
    category: str
    quantity: int
    price: float


class SProduct(SProductAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)


class SProductId(BaseModel):
    ok: bool = True
    product_id: int


class SBasketAdd(BaseModel):
    pr_category: str
    cust_id: int
    quantity: int


class SBasket(BaseModel):
    id: int
    pr_category: str
    cust_id: int
    pr_price: float
    quantity: int


class SBasketId(BaseModel):
    ok: bool = True
    basket_id: int


class SPurchase(BaseModel):
    id: int
    cust_id: int
    time: datetime
    total_cost: float
    pr_list: List[dict]


class SPurchaseId(BaseModel):
    purchase_id: int
