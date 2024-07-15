from sqlalchemy import select

from database import new_session, Supplies
from schemas import SSupplyAdd, SSupply


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
    async def find_all(cls) -> list[SSupply]:
        async with new_session() as session:
            query = select(Supplies)
            result = await session.execute(query)
            supply_models = result.scalars().all()
            supply_schemas = [SSupply.model_validate(supply_model) for supply_model in supply_models]
            return supply_schemas


