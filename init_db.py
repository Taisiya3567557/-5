import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Удалим таблицы, если они уже существуют
cursor.execute("DROP TABLE IF EXISTS WebUsers")
cursor.execute("DROP TABLE IF EXISTS AppUsers")

# Создаем таблицы
cursor.execute("""
CREATE TABLE WebUsers (
    UserID INTEGER PRIMARY KEY,
    UserName TEXT
)
""")

cursor.execute("""
CREATE TABLE AppUsers (
    UserID INTEGER PRIMARY KEY,
    UserName TEXT
)
""")

# Пример данных
web_users = [
    (1, 'Alice'),
    (2, 'Bob'),
    (3, 'Charlie'),
    (4, 'Diana')
]

app_users = [
    (2, 'Bob'),
    (3, 'Charlie'),
    (5, 'Eve')
]

cursor.executemany("INSERT INTO WebUsers VALUES (?, ?)", web_users)
cursor.executemany("INSERT INTO AppUsers VALUES (?, ?)", app_users)

conn.commit()
conn.close()

print("✅ База данных инициализирована.")
