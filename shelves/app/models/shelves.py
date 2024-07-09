from sqlmodel import SQLModel, Field


class ShelfBase(SQLModel):
    shelf_type: str
    volume: int
    is_full: bool | None = None


class Shelf(ShelfBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)


class ShelfCreate(SQLModel):
    shelf_type: str
    volume: int