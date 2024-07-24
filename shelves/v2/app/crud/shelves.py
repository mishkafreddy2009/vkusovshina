from crud.base import CRUDBase
from models.models import Shelf
from models.models import ShelfCreate
from models.models import ShelfUpdate


CRUDShelf = CRUDBase[Shelf, ShelfCreate, ShelfUpdate]
crud_shelf = CRUDShelf(Shelf)