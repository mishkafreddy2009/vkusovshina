from __future__ import annotations

from sqlmodel import Relationship, SQLModel, Field

# from .product import Product


class StorageBase(SQLModel):
    title: str = Field(max_length=255)
    address: str = Field(max_length=255)
    phone_number: str = Field(min_length=11, max_length=11)
    capacity: int = 5000
    current_stock: int = 0


class StorageCreate(StorageBase):
    pass


class StoragePublic(StorageBase):
    id: int


class StorageUpdate(StorageBase):
    title: str | None = Field(default=None, max_length=255)


class Storage(StorageBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
    products: list["Product"] = Relationship(
            back_populates="storage", 
            sa_relationship_kwargs={"lazy": "selectin"}
            )


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


