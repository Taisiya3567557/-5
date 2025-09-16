import sqlite3

conn = sqlite3.connect('social_network.db')
cursor = conn.cursor()

# Создаем таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Posts (
    post_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    post_content TEXT,
    likes_count INTEGER DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
''')

# Вставляем тестовые данные
cursor.execute("INSERT OR IGNORE INTO Users (user_id, username) VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie');")

cursor.execute("INSERT OR IGNORE INTO Posts (post_id, user_id, post_content, likes_count) VALUES \
(1, 1, 'Post by Alice 1', 5), \
(2, 1, 'Post by Alice 2', 3), \
(3, 2, 'Post by Bob 1', 7);")

conn.commit()
conn.close()

print("Database setup complete.")
