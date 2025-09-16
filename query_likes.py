import sqlite3

conn = sqlite3.connect('social_network.db')
cursor = conn.cursor()

query = '''
SELECT 
    u.user_id, 
    u.username, 
    COALESCE(SUM(p.likes_count), 0) AS total_likes
FROM 
    Users u
LEFT JOIN 
    Posts p ON u.user_id = p.user_id
GROUP BY 
    u.user_id, u.username
ORDER BY 
    total_likes DESC;
'''

cursor.execute(query)
results = cursor.fetchall()

for row in results:
    print(f"User ID: {row[0]}, Username: {row[1]}, Total Likes: {row[2]}")

conn.close()
