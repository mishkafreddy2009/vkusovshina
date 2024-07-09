from sqlmodel import SQLModel, Field


class StorageBase(SQLModel):
    name: str
    address: str
    phone_number: str
    is_full: bool | None = None


class Storage(StorageBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)


class StorageCreate(SQLModel):
    name: str
    address: str
    phone_number: str
