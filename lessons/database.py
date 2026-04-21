
def create_tables(conn):
    conn.execute("DROP TABLE IF EXISTS students")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        city TEXT
    )
    """)

def add_student(conn, name, age, city):
    print(name, age, city)
    conn.execute("""
    INSERT INTO students (name, age, city)
    VALUES (?, ?, ?)
    """, (name, age, city))
    conn.commit()

def get_all_students(conn):
    # result = conn.execute("""
    # SELECT name FROM students
    # """)
    result = conn.execute("""
    SELECT * FROM students
    """)
    return result.fetchall()

def get_one_student(conn, student_id):
    result = conn.execute("""
    SELECT * FROM students WHERE id = ?
    """, (student_id,))
    return result.fetchall()

def get_students_by_name(conn, name):
    result = conn.execute("""
    SELECT * FROM students WHERE name = ?
    """, (name,))
    return result.fetchall()

def delete_student(conn, student_id):
    conn.execute("""
    DELETE FROM students WHERE id = ?
    """, (student_id,))
    conn.commit()

def delete_by_city(conn, city):
    conn.execute("""
    DELETE FROM students WHERE city = ?
    """, (city,))
    conn.commit()

def change_student(
    conn,
    student_id,
    name,
    age,
    city,
):
    conn.execute("""
    UPDATE students SET 
    name = ?, 
    age = ?, 
    city = ? 
    WHERE id = ?             
    """,
    (name, age, city, student_id))
    conn.commit()