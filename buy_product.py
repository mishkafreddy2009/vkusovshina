# v 0.01
class Customer:
    def __init__(self, customer_id: int, first_name: str, last_name: str, phone_number: str):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def __repr__(self) -> str:
        return f"Customer(id={self.customer_id}, first_name={self.first_name}, last_name={self.last_name}, phone_number={self.phone_number})"

class Product:
    def __init__(self, product_id: int, pr_category_id: int, quantity: int, price: float):
        self.product_id = product_id
        self.pr_category_id = pr_category_id
        self.quantity = quantity
        self.price = price

    def __repr__(self) -> str:
        return f"Product(id={self.product_id}, pr_category_id={self.pr_category_id}, quantity={self.quantity}, price={self.price})"

class Basket:
    def __init__(self, cust_id: int, cust_fname: str, cust_lname: str):
        self.cust_id = cust_id
        self.cust_fname = cust_fname
        self.cust_lname = cust_lname
        self.items = []

    def add_to_basket(self, product_id: int, database: list):
        # Поиск продукта в базе данных по product_id
        product = next((p for p in database if p.product_id == product_id and p.quantity > 0), None)

        if product:
            self.items.append(product)
            print(f"Товар {product.product_id} добавлен в корзину.")
            return True
        else:
            print("Товар не найден или отсутствует на складе.")
            return False

    def complete_purchase(self, database: list):

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
    
    def __repr__(self) -> str:
        return f"Basket(cust_id={self.cust_id}, cust_fname={self.cust_fname}, cust_lname={self.cust_lname}, items={self.items})"


# Имитация базы данных продуктов
database = [
    Product(1, 100, 10, 5.99),
    Product(2, 101, 5, 3.49),
    Product(3, 102, 0, 4.99),  # Продукт закончился на складе
]

# Создание покупателя
customer = Customer(1, "Ivan", "Ivanov", "1234567890")

# Создание корзины
basket = Basket(customer.customer_id, customer.first_name, customer.last_name)

# Покупатель хочет купить продукт с id 1 (например, колбаса)
if basket.add_to_basket(1, database):
    basket.complete_purchase(database)

# Покупатель хочет купить продукт с id 3 (нет в наличии)
basket.add_to_basket(3, database)

# Покупатель хочет купить продукт с id 2 (например, хлеб)
if basket.add_to_basket(2, database):
    basket.complete_purchase(database)

# Вывод текущего состояния базы данных
print("Текущее состояние базы данных продуктов:")

for product in database:
    print(product)

#done:
#Поиск продукта, удаление продукта, классы корзины, покупателя, продукта
#to do:
#Связать функции с SQL, проверить работу на SQL