"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv


def executing_sql(query):

    """ Функция для установления соединения и выполнения запросов. """

    connect = psycopg2.connect(host="localhost", port="5432", database="north", user="postgres", password="")
    try:
        with connect:
            with connect.cursor() as cursor:
                cursor.execute(query)
    finally: connect.close()


def filling_in_tables(table_name, file_csv):

    """ Функция для заполнения таблиц. """

    with open(file_csv, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            values = "', '".join(row)
            query = f"INSERT INTO {table_name} VALUES ('{values}');"
            executing_sql(query)


# Заполнение таблицы employees данными
employees_csv = 'north_data/employees_data.csv'
filling_in_tables('employees', employees_csv)

# Заполнение таблицы customers данными
#customers_csv = 'north_data/customers_data.csv'
#filling_in_tables('customers', customers_csv)

# Заполнение таблицы orders данными
orders_csv = 'north_data/orders_data.csv'
filling_in_tables('orders', orders_csv)