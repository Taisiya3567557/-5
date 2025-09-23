import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# SQL-запрос для нахождения пользователей и сайта, и приложения
cursor.execute("""
SELECT WebUsers.UserID, WebUsers.UserName
FROM WebUsers
INNER JOIN AppUsers ON WebUsers.UserID = AppUsers.UserID
""")

results = cursor.fetchall()

print("👥 Пользователи, которые пользуются и сайтом, и приложением:")
for user_id, user_name in results:
    print(f"- {user_id}: {user_name}")

conn.close()
