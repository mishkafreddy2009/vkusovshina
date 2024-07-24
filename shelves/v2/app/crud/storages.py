from crud.base import CRUDBase
from models.models import Storage
from models.models import StorageCreate
from models.models import StorageUpdate


CRUDStorage = CRUDBase[Storage, StorageCreate, StorageUpdate]
crud_storage = CRUDStorage(Storage)