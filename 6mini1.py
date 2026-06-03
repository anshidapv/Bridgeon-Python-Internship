import json
students = [
    {"name": "riya", "age": 19, "mark": 78},
    {"name": "sara", "age": 20, "mark": 90},
    {"name": "tommy", "age": 19, "mark": 85},
    {"name": "john", "age": 21, "mark": 92},
    {"name": "ziya", "age": 20, "mark": 89}
]
with open("students.json", "w") as file:
    json.dump(students, file, indent=2)
print("data saved successfully")
with open("students.json", "r") as file:
    print(file.read())
     