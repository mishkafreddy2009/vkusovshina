from datetime import datetime
from typing import Dict, Any

from sqlalchemy import select, update, delete
from sqlalchemy.orm import InstrumentedAttribute
from sqlalchemy.orm.base import _T_co

from database import new_session, ProductTable, BasketTable, PurchaseTable, User
from models import user
from schemas import SProductAdd, SProduct, SBasketAdd, SBasket, SPurchase, UserRead

# для работы с продуктами
class ProductRepository:
    @classmethod
    async def add_one(cls, data: SProductAdd) -> dict[str, Any] | InstrumentedAttribute[_T_co] | _T_co:
        async with new_session() as session:
            # product_query = select(ProductTable).where(ProductTable.category == data.pr_category)
            # product_result = await session.execute(product_query)
            # product = product_result.scalar_one_or_none()
            #
            # if not product or product.quantity < data.quantity:
            #     raise ValueError("Insufficient product quantity or product not found")

            product_check = select(ProductTable).where(ProductTable.category == data.category)
            product_result = await session.execute(product_check)
            product_exist = product_result.scalar_one_or_none()

            if product_exist:
                product_exist.quantity += data.quantity
                await session.flush()
                await session.commit()
                return product_exist.id

            product_dict = data.model_dump()
            product = ProductTable(**product_dict)
            session.add(product)
            await session.flush()
            await session.commit()
            return product.id

    @classmethod
    async def find_all(cls) -> list[SProduct]:
        async with new_session() as session:
            query = select(ProductTable)
            result = await session.execute(query)
            product_models = result.scalars().all()
            product_schemas = [SProduct.model_validate(product_model) for product_model in product_models]
            return product_schemas

    # придумать реализацию
    @classmethod
    async def update_quantity(cls, category: str, quantity: int) -> bool:
        async with new_session() as session:
            query = update(ProductTable).where(ProductTable.category == category).values(quantity=quantity)
            await session.execute(query)
            await session.commit()
            return True


# для работы с карзиной
class BasketRepository:
    @classmethod
    async def add_one(cls, data: SBasketAdd, customer: user) -> int:
        async with new_session() as session:
            product_query = select(ProductTable).where(ProductTable.category == data.pr_category)
            product_result = await session.execute(product_query)
            product = product_result.scalar_one_or_none()

            if not product or product.quantity < data.quantity:
                raise ValueError("Insufficient product quantity or product not found")

            # изменение количества + подсчет стоимости
            product.quantity -= data.quantity
            cost = product.price * data.quantity

            basket_dict = {
                "pr_category": data.pr_category,
                "cust_id": customer.id,
                "pr_price": cost,
                "quantity": data.quantity,
            }
            basket = BasketTable(**basket_dict)
            session.add(basket)
            await session.flush()
            await session.commit()
            return basket.id

    @classmethod
    async def find_all(cls) -> list[SBasket]:
        async with new_session() as session:
            query = select(BasketTable)
            result = await session.execute(query)
            basket_models = result.scalars().all()
            basket_schemas = [SBasket.model_validate(basket_model.__dict__) for basket_model in basket_models]
            return basket_schemas


#для работы с покупками
class PurchaseRepository:

    @classmethod
    async def complete_purchase(cls):
        async with new_session() as session:
            async with session.begin():
                # Получаем все элементы из корзины
                query = select(BasketTable)
                result = await session.execute(query)
                basket_models = result.scalars().all()

                if not basket_models:
                    return False
                # Создаём список для pr_list
                pr_list = []
                total_cost = 0

                # Переносим товары в purchases и подсчитываем общую стоимость
                for basket_model in basket_models:
                    pr_list.append({
                        "pr_category": basket_model.pr_category,
                        "quantity": basket_model.quantity,
                        "pr_price": basket_model.pr_price
                    })
                    total_cost += basket_model.pr_price

                # Создаём запись в таблице purchases
                purchase = PurchaseTable(
                    cust_id=basket_model.cust_id,
                    time=datetime.now(),
                    total_cost=total_cost,
                    pr_list=pr_list
                )
                session.add(purchase)

                # Очищаем корзину
                delete_query = delete(BasketTable)
                await session.execute(delete_query)
                await session.commit()
                return purchase.id

    @classmethod
    async def find_all(cls) -> list[SPurchase]:
        async with new_session() as session:
            query = select(PurchaseTable)
            result = await session.execute(query)
            purchase_models = result.scalars().all()
            purchase_schemas = [SPurchase.model_validate(purchase_model.__dict__) for purchase_model in purchase_models]
            return purchase_schemas


#для работы с пользователем
class UserRepository:
    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(User)
            result = await session.execute(query)
            user_models = result.scalars().all()
            user_schemas = [UserRead.model_validate(basket_model.__dict__) for basket_model in user_models]
            return user_schemas
