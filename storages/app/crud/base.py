from collections.abc import Sequence
from typing import Any, Generic, Type, TypeVar, Union

from sqlmodel import SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=SQLModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=SQLModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]) -> None:
        self._model = model

    async def create(self, session: AsyncSession, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = dict(obj_in)
        db_obj = self._model(**obj_in_data)
        session.add(db_obj)
        await session.commit()
        return db_obj

    async def get(self, session: AsyncSession, *args, **kwargs) -> ModelType | None:
        result = await session.exec(select(self._model).filter(*args).filter_by(**kwargs))
        return result.first()

    async def get_multi(self, session: AsyncSession, *args, offset: int = 0, limit: int = 100, **kwargs) -> Sequence[ModelType]:
        result = await session.exec(select(self._model).filter(*args).filter_by(**kwargs).offset(offset).limit(limit))
        return result.all()

    async def update(self, session: AsyncSession, *, obj_in: Union[UpdateSchemaType, dict[str, Any]], db_obj: ModelType | None = None, **kwargs) -> ModelType | None:
        db_obj = db_obj or await self.get(session, **kwargs)
        if db_obj:
            obj_data = db_obj.model_dump()
            if isinstance(obj_in, dict):
                update_data = obj_in
            else:
                update_data = obj_in.model_dump(exclude_unset=True)
            for field in obj_data:
                if field in update_data:
                    setattr(db_obj, field, update_data[field])
            session.add(db_obj)
            await session.commit()
        return db_obj
