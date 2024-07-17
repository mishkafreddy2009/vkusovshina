# from __future__ import annotations
# from typing import TYPE_CHECKING

# from sqlmodel import Relationship
from sqlmodel import SQLModel
from sqlmodel import Field

# if TYPE_CHECKING:
#     from .storage import Storage
# from .storage import Storage


class ProductBase(SQLModel):
    title: str = Field(max_length=255)
    description: str | None = Field(default=None, max_length=255)
    quantity: int = 0


class Product(ProductBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
    storage_id: int = Field(default=None, foreign_key="storage.id")
    # storage: Storage = Relationship(back_populates="products")


class ProductCreate(ProductBase):
    pass


class ProductPublic(ProductBase):
    id: int
    storage_id: int


class ProductUpdate(ProductBase):
    title: str | None = Field(default=None, max_length=255) # type: ignore
