import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute(
    "SELECT*FROM students WHERE marks > ?",
    (70,)
)
rows = cursor.fetchall()
print("students with marks above 70:")
print("-"*35)
for row in rows:
    print(f"id: {row[0]}, name: {row[1]}, marks: {row[2]}")
    conn.close()