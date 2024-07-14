from sqlalchemy import select

from database import new_session, Supplies
from schemas import SSupplyAdd


class SuppliesRepository:
    @classmethod
    async def add_one(cls, data: SSupplyAdd) -> int:
        async with new_session() as session:
            supply_dict = data.model_dump()

            supply = Supplies(**supply_dict)
            session.add(supply)
            await session.flush()
            await session.commit()
            return supply.id


    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(Supplies)
            result = await session.execute(query)
            supply_models = result.scalars().all()
            return supply_models


