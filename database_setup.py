import sqlite3

# Подключаемся к базе данных (если базы нет, она будет создана)
connection = sqlite3.connect('company.db')
cursor = connection.cursor()

# Создание таблиц
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT,
    department TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY,
    project_name TEXT,
    employee_id INTEGER,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);
''')

# Добавление тестовых данных
cursor.execute("INSERT INTO employees (employee_name, department) VALUES ('Alice', 'IT')")
cursor.execute("INSERT INTO employees (employee_name, department) VALUES ('Bob', 'HR')")
cursor.execute("INSERT INTO employees (employee_name, department) VALUES ('Charlie', 'Finance')")

cursor.execute("INSERT INTO projects (project_name, employee_id) VALUES ('Project X', 1)")
cursor.execute("INSERT INTO projects (project_name, employee_id) VALUES ('Project Y', 2)")

# Сохраняем изменения
connection.commit()

# Закрытие соединения
connection.close()

print("База данных и таблицы успешно созданы и заполнены.")
