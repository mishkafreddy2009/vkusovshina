from app.crud.base import CRUDBase
from app.models.storage import Product
from app.models.storage import ProductCreate
from app.models.storage import ProductUpdate

CRUDProduct = CRUDBase[Product, ProductCreate, ProductUpdate]
crud_product = CRUDProduct(Product)
