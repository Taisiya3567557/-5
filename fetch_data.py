import sqlite3
import pandas as pd

# Подключаемся к базе данных
conn = sqlite3.connect('cinema.db')

# SQL-запрос для получения всех данных (без фильтрации)
query = '''
SELECT 
    m.Title AS MovieTitle,
    g.GenreName AS Genre,
    s.SessionDate AS SessionDate,
    c.FirstName || ' ' || c.LastName AS CustomerName,
    c.City AS CustomerCity,
    s.TicketPrice AS TicketPrice
FROM 
    Tickets t
JOIN 
    Sessions s ON t.SessionID = s.SessionID
JOIN 
    Movies m ON s.MovieID = m.MovieID
JOIN 
    Genres g ON m.GenreID = g.GenreID
JOIN 
    Customers c ON t.CustomerID = c.CustomerID
ORDER BY 
    s.SessionDate;
'''

# Выполняем запрос и загружаем результат в DataFrame
df = pd.read_sql(query, conn)

# Закрываем соединение
conn.close()

# Выводим результат
print(df)
