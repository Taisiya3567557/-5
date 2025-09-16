import sqlite3

def run_query(query):
    """Функция для выполнения SQL-запроса и вывода результатов."""
    connection = sqlite3.connect('company.db')
    cursor = connection.cursor()
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    connection.close()
    return results

# Задача 1: Показать всех сотрудников и проекты, в которых они участвуют
def task_1():
    query_1 = """
    SELECT employees.employee_id, employees.employee_name, projects.project_name
    FROM employees
    LEFT OUTER JOIN projects ON employees.employee_id = projects.employee_id;
    """
    results = run_query(query_1)
    print("Задача 1:")
    for row in results:
        print(row)

# Задача 2: Показать все проекты и сотрудников, которые над ними работают
def task_2():
    query_2 = """
    SELECT projects.project_id, projects.project_name, employees.employee_name
    FROM projects
    LEFT OUTER JOIN employees ON projects.employee_id = employees.employee_id;
    """
    results = run_query(query_2)
    print("\nЗадача 2:")
    for row in results:
        print(row)

# Задача 3: Вывести список всех сотрудников, которые не работают над никаким проектом
def task_3():
    query_3 = """
    SELECT employees.employee_id, employees.employee_name
    FROM employees
    LEFT OUTER JOIN projects ON employees.employee_id = projects.employee_id
    WHERE projects.project_id IS NULL;
    """
    results = run_query(query_3)
    print("\nЗадача 3:")
    for row in results:
        print(row)

# Задача 4: Показать всех сотрудников и все проекты
def task_4():
    query_4 = """
    SELECT employees.employee_id, employees.employee_name, projects.project_id, projects.project_name
    FROM employees
    FULL OUTER JOIN projects ON employees.employee_id = projects.employee_id;
    """
    results = run_query(query_4)
    print("\nЗадача 4:")
    for row in results:
        print(row)
