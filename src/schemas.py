from datetime import datetime
from typing import Optional, List

from fastapi_users import schemas
from pydantic import BaseModel, ConfigDict


class SProductAdd(BaseModel):
    category: str
    quantity: int
    price: float


class SProduct(SProductAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)


class SBasketAdd(BaseModel):
    pr_category: str
    quantity: int


class SBasket(BaseModel):
    id: int
    pr_category: str
    cust_id: int
    pr_price: float
    quantity: int


class SPurchase(BaseModel):
    id: int
    cust_id: int
    time: datetime
    total_cost: float
    pr_list: List[dict]


#добавляем пользователя
class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
