import psycopg2
import csv
conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='********' #надеюсь, пароль не понадобится для проерки д.з.? Не знала, что он будет так виден.
)
try:
    with conn:
        with conn.cursor() as cur:
            with open('employees_data.csv') as r_file:
                reader = csv.DictReader(r_file)
                num = 1
                for row in reader:
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s )",
                                (
                                    num,
                                    row['first_name'],
                                    row['last_name'],
                                    row['title'],
                                    row['birth_date'],
                                    row['notes'])
                                )
                    num +=1
            with open('customers_data.csv') as r_file:
                reader = csv.DictReader(r_file)
                for row in reader:
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                                (
                                    row['customer_id'],
                                    row['company_name'],
                                    row['contact_name']
                                )
                                )
            with open('orders_data.csv') as r_file:
                reader = csv.DictReader(r_file)
                for row in reader:
                    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                                (
                                    row['order_id'],
                                    row['customer_id'],
                                    row['employee_id'],
                                    row['order_date'],
                                    row['ship_city']
                                )
                                )
finally:
    conn.close()
