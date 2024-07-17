from __future__ import annotations
# from typing import TYPE_CHECKING

# from sqlmodel import Relationship
from sqlmodel import SQLModel
from sqlmodel import Field

# if TYPE_CHECKING:
#     from .product import Product


class StorageBase(SQLModel):
    title: str = Field(default="Большой склад №1", max_length=255)
    description: str | None = Field(default="Самый большой склад.", max_length=255)
    address: str = Field(default="ул. Ленина д. 23", max_length=255)
    phone_number: str = Field(default="79823069920", max_length=11)
    capacity: int = 5000
    current_stock: int = 0
    is_full: bool = False


class StorageCreate(StorageBase):
    pass


class StoragePublic(StorageBase):
    id: int


class StorageUpdate(StorageBase):
    title: str | None = Field(default=None, max_length=255) # type: ignore


class Storage(StorageBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
    # products: list["Product"] = Relationship(
    #         back_populates="storage", 
    #         sa_relationship_kwargs={"lazy": "selectin"}
    #         )
