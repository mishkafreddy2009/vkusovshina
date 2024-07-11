from app.crud.base import CRUDBase
from app.models.models import Storage
from app.models.models import StorageCreate
from app.models.models import StorageUpdate

CRUDStorage = CRUDBase[Storage, StorageCreate, StorageUpdate]
crud_storage = CRUDStorage(Storage)
