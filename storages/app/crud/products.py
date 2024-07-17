from app.crud.base import CRUDBase
from app.models.product import Product
from app.models.product import ProductCreate
from app.models.product import ProductUpdate

CRUDProduct = CRUDBase[Product, ProductCreate, ProductUpdate]
crud_product = CRUDProduct(Product)
