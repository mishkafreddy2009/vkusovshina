from pydantic import BaseModel


class Storage(BaseModel):
    title: str
    address: str
    phone_number: str


class StorageIn(BaseModel):
    title: str
    address: str
    phone_number: str


class StorageOut(StorageIn):
    id: int


class StorageUpdate(StorageIn):
    title: str | None = None
    address: str | None = None
    phone_number: str | None = None
