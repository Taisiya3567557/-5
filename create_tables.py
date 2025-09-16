import sqlite3

# Создание базы данных и подключение
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Создание таблиц
cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INTEGER PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    DepartmentID INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Departments (
    DepartmentID INTEGER PRIMARY KEY,
    DepartmentName TEXT,
    ManagerID INTEGER
)
''')

# Вставка данных
cursor.execute("INSERT INTO Departments VALUES (1, 'IT', 101)")
cursor.execute("INSERT INTO Departments VALUES (2, 'HR', 102)")

cursor.execute("INSERT INTO Employees VALUES (1, 'Alice', 'Smith', 1)")
cursor.execute("INSERT INTO Employees VALUES (2, 'Bob', 'Johnson', 2)")
cursor.execute("INSERT INTO Employees VALUES (3, 'Charlie', 'Lee', NULL)")  # без отдела

conn.commit()
conn.close()
