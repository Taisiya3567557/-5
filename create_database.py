import sqlite3

# Подключаемся к базе данных (она будет создана, если не существует)
conn = sqlite3.connect('cinema.db')
cursor = conn.cursor()

# Создаем таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS Movies (
    MovieID INTEGER PRIMARY KEY,
    Title TEXT,
    Year INTEGER,
    GenreID INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Genres (
    GenreID INTEGER PRIMARY KEY,
    GenreName TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Sessions (
    SessionID INTEGER PRIMARY KEY,
    MovieID INTEGER,
    HallID INTEGER,
    SessionDate TEXT,
    TicketPrice REAL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Halls (
    HallID INTEGER PRIMARY KEY,
    HallName TEXT,
    Capacity INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Tickets (
    TicketID INTEGER PRIMARY KEY,
    SessionID INTEGER,
    CustomerID INTEGER,
    SeatNumber INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INTEGER PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    City TEXT
)
''')

# Добавление тестовых данных
cursor.executemany('''
INSERT INTO Genres (GenreID, GenreName) VALUES (?, ?)
''', [
    (1, 'Action'),
    (2, 'Comedy'),
    (3, 'Drama')
])

cursor.executemany('''
INSERT INTO Movies (MovieID, Title, Year, GenreID) VALUES (?, ?, ?, ?)
''', [
    (1, 'Movie 1', 2021, 1),
    (2, 'Movie 2', 2022, 2),
    (3, 'Movie 3', 2023, 3)
])

cursor.executemany('''
INSERT INTO Halls (HallID, HallName, Capacity) VALUES (?, ?, ?)
''', [
    (1, 'Hall 1', 100),
    (2, 'Hall 2', 120)
])

cursor.executemany('''
INSERT INTO Sessions (SessionID, MovieID, HallID, SessionDate, TicketPrice) VALUES (?, ?, ?, ?, ?)
''', [
    (1, 1, 1, '2023-09-20 14:00', 10.0),
    (2, 2, 2, '2023-09-20 16:00', 12.0),
    (3, 3, 1, '2023-09-21 18:00', 8.0)
])

cursor.executemany('''
INSERT INTO Customers (CustomerID, FirstName, LastName, City) VALUES (?, ?, ?, ?)
''', [
    (1, 'John', 'Doe', 'New York'),
    (2, 'Jane', 'Smith', 'Los Angeles'),
    (3, 'Mike', 'Jordan', 'Chicago')
])

cursor.executemany('''
INSERT INTO Tickets (TicketID, SessionID, CustomerID, SeatNumber) VALUES (?, ?, ?, ?)
''', [
    (1, 1, 1, 1),
    (2, 1, 1, 2),
    (3, 2, 1, 3),
    (4, 3, 2, 4),
    (5, 3, 3, 5)
])

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()

print("База данных создана и данные добавлены.")
