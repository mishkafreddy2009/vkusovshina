from typing import Annotated
from fastapi import APIRouter, Depends

from repository import SuppliesRepository
from schemas import SSupplyAdd


router = APIRouter(
    prefix="/supplies",
)


@router.post("")
async def add_supply(
        supply: Annotated[SSupplyAdd, Depends()]
):
    supply_id = await SuppliesRepository.add_one(supply)
    return {"ok": True, "supply_id": supply_id}


@router.get("")
async def get_supplies():
    supplies = await SuppliesRepository.find_all()
    return {"supplies": supplies}

