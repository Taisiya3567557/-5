import sqlite3

# Создание подключения к базе данных
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Создание таблиц
cursor.executescript("""
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Suppliers;

CREATE TABLE Customers (
    Name TEXT,
    Phone TEXT
);

CREATE TABLE Employees (
    Name TEXT,
    Phone TEXT
);

CREATE TABLE Suppliers (
    Name TEXT,
    Phone TEXT
);
""")

# Пример данных
cursor.executemany("INSERT INTO Customers (Name, Phone) VALUES (?, ?)", [
    ('Анна', '123'),
    ('Борис', None),
    ('Вера', '555'),
])

cursor.executemany("INSERT INTO Employees (Name, Phone) VALUES (?, ?)", [
    ('Георгий', '789'),
    ('Анна', '123'),  # дубликат
    ('Дина', None),
])

cursor.executemany("INSERT INTO Suppliers (Name, Phone) VALUES (?, ?)", [
    ('Елена', '000'),
    ('Борис', None),   # дубликат
    ('Жанна', '555'),  # дубликат по телефону
])

# Выполняем объединение с подстановкой и удалением дубликатов
query = """
SELECT DISTINCT Name, 
       COALESCE(Phone, 'Номер не указан') AS Phone
FROM (
    SELECT Name, Phone FROM Customers
    UNION ALL
    SELECT Name, Phone FROM Employees
    UNION ALL
    SELECT Name, Phone FROM Suppliers
)
"""

print("Общий список всех людей с телефонами:\n")

for row in cursor.execute(query):
    print(f"{row[0]} — {row[1]}")

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
