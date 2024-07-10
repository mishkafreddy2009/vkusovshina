# v 0.04
from pydantic import BaseModel, Field, PositiveInt, constr
from datetime import datetime
import time
from typing import List
import psycopg2

# Установление соединения с базой данных
connection = psycopg2.connect(
    host="127.0.0.1",
    user="postgres",
    password="1234",
    database="mydatabase"
)

connection.autocommit = True


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


class Basket(BaseModel):
    cust_id: PositiveInt
    cust_fname: constr(min_length=1)
    cust_lname: constr(min_length=1)
    items: List[Product] = Field(default_factory=list)
    

    def add_to_basket(self, product_id: int) -> bool:

        with connection.cursor() as cursor:
            cursor.execute("SELECT product_id, pr_category_id, quantity, price FROM product_db WHERE product_id = %s AND quantity > 0", (product_id,))
            product_data = cursor.fetchone()

            if product_data:
                product = Product(product_id=product_data[0], pr_category_id=product_data[1], quantity=product_data[2], price=product_data[3])
                self.items.append(product)
                print(f"Товар {product.product_id} добавлен в корзину.")
                return True
            else:
                print(f"Товар {product_id} не найден или отсутствует на складе.")
                return False


    def complete_purchase(self):

        with connection.cursor() as cursor:
            if not self.items:
                print("Корзина пуста. Нечего покупать.")
                return

            purchase_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            total_cost = sum(item.price for item in self.items)
            product_ids = [item.product_id for item in self.items]

            # Вставка записи о покупке
            cursor.execute(
                "INSERT INTO purchases (cust_id, purch_time, total_cost, pr_list) VALUES (%s, %s, %s, %s) RETURNING purch_id",
                (self.cust_id, purchase_time, total_cost, product_ids)
            )
            purch_id = cursor.fetchone()[0]

            # Обновление количества продуктов в базе данных
            for item in self.items:
                cursor.execute("UPDATE product_db SET quantity = quantity - 1 WHERE product_id = %s", (item.product_id,))

            self.items = []
            print(f"Покупка совершена успешно. ID покупки: {purch_id}, Время: {purchase_time}, Стоимость: {total_cost}")
            time.sleep(1)  # чисто визуал


# Создание покупателя
with connection.cursor() as cursor:
    cursor.execute(
        "INSERT INTO customers (first_name, last_name, phone_number) VALUES (%s, %s, %s) RETURNING customer_id",
        ("Ivan", "Ivanov", "1234567890")
    )
    customer_id = cursor.fetchone()[0]

customer = Customer(
    customer_id=customer_id,
    first_name="Ivan",
    last_name="Ivanov",
    phone_number="1234567890"
)

# Создание корзины
basket = Basket(
    cust_id=customer.customer_id,
    cust_fname=customer.first_name,
    cust_lname=customer.last_name
)

basket.add_to_basket(1)
basket.add_to_basket(1)
basket.add_to_basket(1)
basket.add_to_basket(1)
basket.add_to_basket(2)
basket.complete_purchase()



# Покупатель хочет купить продукт с id 1 (например, колбаса)
if basket.add_to_basket(1):
    basket.complete_purchase()

# Покупатель хочет купить продукт с id 3 (нет в наличии)
basket.add_to_basket(3)

# Покупатель хочет купить продукт с id 2 (например, хлеб)
if basket.add_to_basket(2):
    basket.complete_purchase()

# Вывод текущего состояния базы данных продуктов
print("\nТекущее состояние базы данных продуктов:")
with connection.cursor() as cursor:
    cursor.execute("SELECT product_id, pr_category_id, quantity, price FROM product_db")
    products = sorted(cursor.fetchall())

    for product in products:
        print(f"ID: {product[0]}, Категория: {product[1]}, Количество: {product[2]}, Цена: {product[3]}")

    cursor.execute("SELECT purch_id, cust_id, purch_time, total_cost, pr_list FROM purchases")
    purchases = sorted(cursor.fetchall())
    print()

    for purchase in purchases:
        print(f"ID: {purchase[0]}, id покупателя: {purchase[1]}, Время покупки: {purchase[2]}, Стоимость: {purchase[3]}, список продуктов: {purchase[4]}")


#done:
#Поиск продукта, удаление продукта, классы корзины, покупателя, продукта
#Добавлен pydantic, basket -> busket
#Добавлен класс Purchase, и имитация покупки с отправкой инфы
#Добавленны базы данных
#to do:
#Связать функции с SQL, проверить работу на SQL
#Проверить корректность pydantic (input_json = ... , class.parse_raw(input_json) иль чо там)
#Тесты + доработка