import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
student_name = "ali"
cursor.execute(
    "DELETE FROM students WHERE name = ?", 
    (student_name,)
)
conn.commit()
print(f"{student_name} deleted successfully\n")
cursor.execute("SELECT*FROM students")
rows = cursor.fetchall()
print("remaining students:")
print("-"*30)
for row in rows:
    print(f"id: {row[0]}, name: {row[1]}, marks: {row[2]}")
conn.close()