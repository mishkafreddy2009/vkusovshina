from crud.base import CRUDBase
from models.models import Product
from models.models import ProductCreate
from models.models import ProductUpdate

CRUDProduct = CRUDBase[Product, ProductCreate, ProductUpdate]
crud_product = CRUDProduct(Product)