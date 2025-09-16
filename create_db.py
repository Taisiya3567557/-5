import sqlite3

def create_sample_db(db_path='database.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Создаем таблицу Courses
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Courses (
        course_id INTEGER PRIMARY KEY,
        course_title TEXT NOT NULL
    )
    """)

    # Создаем таблицу Enrollments
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Enrollments (
        enrollment_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        course_id INTEGER,
        enrollment_date TEXT,
        FOREIGN KEY (course_id) REFERENCES Courses(course_id)
    )
    """)

    # Добавляем несколько курсов
    cursor.execute("INSERT INTO Courses (course_id, course_title) VALUES (1, 'Математика')")
    cursor.execute("INSERT INTO Courses (course_id, course_title) VALUES (2, 'Физика')")
    cursor.execute("INSERT INTO Courses (course_id, course_title) VALUES (3, 'История')")

    # Добавляем регистрации только для первых двух курсов
    cursor.execute("INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date) VALUES (1, 101, 1, '2023-01-01')")
    cursor.execute("INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date) VALUES (2, 102, 2, '2023-01-02')")

    conn.commit()
    conn.close()
    print("База данных и таблицы созданы, данные добавлены!")

if __name__ == "__main__":
    create_sample_db()
