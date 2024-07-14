from datetime import datetime
from pydantic import BaseModel


class SSupplyAdd(BaseModel):
    provider_id: int
    store_id: str
    date: datetime


class SSupply(SSupplyAdd):
    id: int