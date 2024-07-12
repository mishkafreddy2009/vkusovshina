#для заполнения/ создания баз данных
#тестовый файл (не для идет в прод)

import psycopg2
#from config import host, user, password, db_name


try:
    # connect to exist database
    connection = psycopg2.connect(
        host="127.0.0.1",
        user="postgres",
        password="1234",
        database="mydatabase"    
    )
    connection.autocommit = True
    
    # the cursor for perfoming database operations
    # cursor = connection.cursor()
    
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        
        print(f"Server version: {cursor.fetchone()}")
        
    #create a new table
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS product_db(
                product_id serial PRIMARY KEY, 
                pr_category_id INT, 
                quantity INT, 
                price FLOAT);""" #другие
        )
        cursor.execute("""CREATE TABLE IF NOT EXISTS customers ( 
                customer_id SERIAL PRIMARY KEY,   
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                phone_number VARCHAR(15) NOT NULL);"""
        )
        cursor.execute("""CREATE TABLE IF NOT EXISTS purchases (
                purch_id SERIAL PRIMARY KEY,
                cust_id INT REFERENCES customers(customer_id),
                purch_time TIMESTAMP NOT NULL,
                total_cost FLOAT NOT NULL,
                pr_list INT[]);"""
        )
        cursor.execute("""CREATE TABLE IF NOT EXISTS busket (
                pr_id SERIAL PRIMARY KEY,
                pr_category_id INT,
                cust_id INT REFERENCES customers(customer_id),
                cost FLOAT NOT NULL);"""
        )
        
    #     # connection.commit()
        print("[INFO] Table created successfully")
        
    # insert data into a table
    with connection.cursor() as cursor:
        # cursor.execute("""INSERT INTO product_db (product_id, pr_category_id, quantity, price) VALUES
        #     (1, 100, 10, 5.99),
        #     (2, 101, 5, 3.49),
        #     (3, 102, 0, 4.99);"""
        # )
        cursor.execute("UPDATE product_db SET quantity = quantity + 10 WHERE product_id = '1'")
        cursor.execute("UPDATE product_db SET quantity = quantity + 10 WHERE product_id = '2'")
        cursor.execute("UPDATE product_db SET quantity = quantity + 10 WHERE product_id = '3'")
        
        print("[INFO] Data was succefully inserted")
        


    # get data from a table
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT product_id FROM product_db WHERE pr_category_id = '100';"""
        )
        
        print(cursor.fetchone())
        
    #delete a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE busket;"""
    #     )
        
    #     print("[INFO] Table was deleted")
    
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")