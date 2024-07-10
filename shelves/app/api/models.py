from pydantic import BaseModel, ValidationError, model_validator, PositiveInt


# временная модель продукта для dev версии
# class Product(BaseModel):
#     product_id: PositiveInt
#     name: str
#     product_type: str
#     description: str


class Shelf(BaseModel):
    shelf_type: str
    volume: PositiveInt
    is_full: bool
    # products: list[Product]

    # @model_validator(mode="before")
    # @classmethod
    # def volume_overflow(cls, data):
    #     if isinstance(data, dict):
    #         vol = data["volume"]
    #         prods = data["products"]
    #         if vol < len(prods):
    #             raise OverflowError(f"The amount of products passed to a shelf overflows its maximum volume (={vol})\n{len(prods)} Products: {prods}")
    #         else:
    #             return data


class ShelfIn(BaseModel):
    shelf_type: str
    volume: PositiveInt
    is_full: bool | None = False


class ShelfOut(ShelfIn):
    id: int


class ShelfUpdate(ShelfIn):
    shelf_type: str | None = None
    volume: PositiveInt | None = None
    is_full: bool | None = None