from app.crud.base import CRUDBase
from app.models.models import Image

CRUDProduct = CRUDBase[Product, ProductCreate, ProductUpdate]
crud_product = CRUDProduct(Product)
