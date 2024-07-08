# v 0.02
from pydantic import BaseModel, Field, PositiveInt, constr
from typing import List  #хз надо нет, вроде с питона 3.9 уже не надо так делать


class Customer(BaseModel):
    customer_id: PositiveInt
    first_name: constr(min_length=1)
    last_name: constr(min_length=1)
    phone_number: constr(min_length=10, max_length=15)


class Product(BaseModel):
    product_id: PositiveInt
    pr_category_id: PositiveInt
    quantity: int
    price: float


class Busket(BaseModel):
    cust_id: PositiveInt
    cust_fname: constr(min_length=1)
    cust_lname: constr(min_length=1)
    items: List[Product] = Field(default_factory=list)


    def add_to_basket(self, product_id: int, database: List[Product]) -> bool:
        # Поиск продукта в базе данных по product_id
        product = next((p for p in database if p.product_id == product_id and p.quantity > 0), None)

        if product:
            self.items.append(product)
            print(f"Товар {product.product_id} добавлен в корзину.")
            return True

        else:
            print("Товар не найден или отсутствует на складе.")
            return False


    def complete_purchase(self, database: List[Product]):

        if not self.items:
            print("Корзина пуста. Нечего покупать.")
            return

        for item in self.items:
            database_item = next((p for p in database if p.product_id == item.product_id), None)

            if database_item:
                database_item.quantity -= 1

                if database_item.quantity == 0:
                    database.remove(database_item)

        self.items = []
        print("Покупка совершена успешно.")


# Имитация базы данных продуктов
database = [
    Product(product_id=1, pr_category_id=100, quantity=10, price=5.99),
    Product(product_id=2, pr_category_id=101, quantity=5, price=3.49),
    Product(product_id=3, pr_category_id=102, quantity=0, price=4.99),  # Продукт закончился на складе
]

# Создание покупателя
customer = Customer(
    customer_id=1,
    first_name="Ivan",
    last_name="Ivanov",
    phone_number="1234567890"
)

# Создание корзины
busket = Busket(
    cust_id=customer.customer_id,
    cust_fname=customer.first_name,
    cust_lname=customer.last_name
)

# Покупатель хочет купить продукт с id 1 (например, колбаса)
if busket.add_to_basket(1, database):
    busket.complete_purchase(database)

# Покупатель хочет купить продукт с id 3 (нет в наличии)
busket.add_to_basket(3, database)

# Покупатель хочет купить продукт с id 2 (например, хлеб)
if busket.add_to_basket(2, database):
    busket.complete_purchase(database)

# Вывод текущего состояния базы данных
print("Текущее состояние базы данных продуктов:")
for product in database:
    print(product)

#done:
#Поиск продукта, удаление продукта, классы корзины, покупателя, продукта
#Добавлен pydantic, basket -> busket
#to do:
#Связать функции с SQL, проверить работу на SQL
#Проверить корректность pydantic (input_json = ... , class.parse_raw(input_json) иль чо там)
