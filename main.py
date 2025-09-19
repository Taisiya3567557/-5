import sqlite3
import pandas as pd

# Подключение к реальному файлу базы данных
conn = sqlite3.connect('data.db')  # будет создан, если не существует
cursor = conn.cursor()

# Создание таблиц и вставка данных
cursor.execute('DROP TABLE IF EXISTS Customers')
cursor.execute('DROP TABLE IF EXISTS Employees')
cursor.execute('DROP TABLE IF EXISTS FilteredPeople')  # если запускать повторно

# Данные
customers = [
    (1, 'Alice', 'Berlin', 'Germany'),
    (2, 'Bob', 'Paris', 'France'),
    (3, 'Charlie', 'Madrid', 'Spain'),
    (4, 'Diana', 'Munich', 'Germany'),
]

employees = [
    (1, 'Eve', 'Paris', 'France'),
    (2, 'Frank', 'Berlin', 'Germany'),
    (3, 'Grace', 'Rome', 'Italy'),
    (4, 'Heidi', 'Lyon', 'France'),
]

# Создание таблиц
cursor.execute('''
    CREATE TABLE Customers (
        CustomerID INTEGER,
        Name TEXT,
        City TEXT,
        Country TEXT
    )
''')
cursor.executemany('INSERT INTO Customers VALUES (?, ?, ?, ?)', customers)

cursor.execute('''
    CREATE TABLE Employees (
        EmployeeID INTEGER,
        Name TEXT,
        City TEXT,
        Country TEXT
    )
''')
cursor.executemany('INSERT INTO Employees VALUES (?, ?, ?, ?)', employees)

# SQL-запрос
query = """
SELECT Name, City, Country, 'Customer' AS Role
FROM Customers
WHERE Country IN ('Germany', 'France')

UNION

SELECT Name, City, Country, 'Employee' AS Role
FROM Employees
WHERE Country IN ('Germany', 'France')
ORDER BY City, Name
"""

# Чтение результата
df = pd.read_sql_query(query, conn)

# Сохраняем результат как новую таблицу в БД
df.to_sql('FilteredPeople', conn, if_exists='replace', index=False)

print("✅ Таблица 'FilteredPeople' создана в базе данных data.db")

# Закрытие подключения
conn.commit()
conn.close()
