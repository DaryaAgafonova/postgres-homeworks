-- SQL-команды для создания таблиц

""" Создание таблицы customers. """
CREATE TABLE customers
(
    customer_id VARCHAR(100) PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    contact_name VARCHAR(100) NOT NULL
);

""" Создание таблицы employees. """
CREATE TABLE employees
(
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    title VARCHAR(100) NOT NULL,
    birth_date DATE,
    notes TEXT
);

""" Создание таблицы orders. """
CREATE TABLE orders
(
    order_id INT PRIMARY KEY,
    customer_id VARCHAR(100) REFERENCES customers(customer_id),
    employee_id INT REFERENCES employees(employee_id),
    order_date DATE,
    ship_city VARCHAR(100) NOT NULL
);