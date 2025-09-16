import sqlite3
import pandas as pd

# Подключение к базе
conn = sqlite3.connect('employees.db')

# Выполнение запроса
query = '''
SELECT 
    e.EmployeeID,
    e.FirstName,
    e.LastName,
    d.DepartmentName
FROM 
    Employees e
INNER JOIN 
    Departments d ON e.DepartmentID = d.DepartmentID
'''

# Используем pandas для красивого вывода
df = pd.read_sql_query(query, conn)
print(df)

conn.close()
