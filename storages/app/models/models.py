from sqlmodel import Relationship, SQLModel, Field


class StorageBase(SQLModel):
    name: str = Field(unique=True, max_length=255)
    description: str = Field(max_length=255)
    address: str = Field(max_length=255)
    phone_number: str = Field(max_length=11)
    capacity: int
    current_stock: int = 0
    is_full: bool = False


class StorageCreate(StorageBase):
    pass


class StoragePublic(StorageBase):
    id: int


class StorageUpdate(StorageBase):
    name: str | None = Field(default=None, max_length=255) # type: ignore


class Storage(StorageBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
    products: list["Product"] = Relationship(
            back_populates="storage", 
            sa_relationship_kwargs={"lazy": "selectin"}
            )


class ProductBase(SQLModel):
    title: str = Field(max_length=255)
    description: str | None = Field(default=None, max_length=255)
    quantity: int = 0


class Product(ProductBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
    storage_id: int = Field(default=None, foreign_key="storage.id")
    storage: Storage | None = Relationship(back_populates="products")


class ProductCreate(ProductBase):
    pass

class ProductPublic(ProductBase):
    id: int
    storage_id: int

class ProductUpdate(ProductBase):
    title: str | None = Field(default=None, max_length=255) # type: ignore
