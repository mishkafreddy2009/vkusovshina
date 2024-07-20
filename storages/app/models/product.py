# from __future__ import annotations
# from typing import TYPE_CHECKING

# from sqlmodel import Relationship
from sqlmodel import SQLModel
from sqlmodel import Field

# if TYPE_CHECKING:
#     from .storage import Storage
# from .storage import Storage


class ProductBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)
    quantity: int = 0


class ProductCreate(ProductBase):
    title: str = Field(min_length=1, max_length=255)


class ProductUpdate(ProductBase):
    title: str | None = Field(default=None, max_length=255) # type: ignore


class Product(ProductBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(max_length=255)
    storage_id: int = Field(default=None, foreign_key="storage.id")


class ProductPublic(ProductBase):
    id: int
    # storage_id: int


