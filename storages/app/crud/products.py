from app.crud.base import CRUDBase
from app.models.models import Product
from app.models.models import ProductCreate
from app.models.models import ProductUpdate

CRUDProduct = CRUDBase[Product, ProductCreate, ProductUpdate]
crud_product = CRUDProduct(Product)
