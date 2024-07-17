from app.crud.base import CRUDBase
from app.models.storage import Storage
from app.models.storage import StorageCreate
from app.models.storage import StorageUpdate

CRUDStorage = CRUDBase[Storage, StorageCreate, StorageUpdate]
crud_storage = CRUDStorage(Storage)
