import  sqlite3
conn = sqlite3.connect("students.db")
cursor= conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL,
    marks INTEGER NOT NULL
)
""")
students = [
    ("lisa", 95),
    ("riya", 80),
    ("zain", 88),
    ("john", 70),
    ("anya", 79)
]
for student in students:
    cursor.execute(
        "insert into students(name, marks) VALUES(?,?)",
        student
    )
conn.commit()
cursor.execute("select*from students")
print("student records:")
for row in cursor.fetchall():
    print(row)
conn.close()
