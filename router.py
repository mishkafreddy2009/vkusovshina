from typing import Annotated
from fastapi import APIRouter, Depends

from repository import SuppliesRepository
from schemas import SSupplyAdd, SSupply, SSupplyId

router = APIRouter(
    prefix="/supplies",
    tags=["Поставки"],
)


@router.post("")
async def add_supply(
        supply: Annotated[SSupplyAdd, Depends()]
) -> SSupplyId:
    supply_id = await SuppliesRepository.add_one(supply)
    return {"ok": True, "supply_id": supply_id}


@router.get("")
async def get_supplies() -> list[SSupply]:
    supplies = await SuppliesRepository.find_all()
    return supplies

