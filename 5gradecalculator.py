class InvalidMarkError(Exception):
    pass


def students(name, *marks):

    if len(marks) == 0:
        print("no marks")

    for m in marks:
        if m < 0 or m > 100:
            raise InvalidMarkError("mark must be 0to 100")

    avg = sum(marks) / len(marks)

    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "F"

    return name, avg, grade


def report(students_list):
    print("-" * 30)
    print(f"{'name':<10}{'average':<10}{'grade':<10}")
    print("-" * 30)

    for student in students_list:
        try:
            name = student[0]
            marks = student[1:]
            result = students(name, *marks)
            print(f"{result[0]:<10}{result[1]:<10.2f}{result[2]:<10}")

        except InvalidMarkError as e:
            print(f"{student[0]:}Error:{e}")

student_data = [
    ("Anshida", 80, 90, 70),    
    ("Riya", 95, 92, 90),       
    ("Jerry", 78, 80, 70),     
    ("Zara", 99,21,42,77),                  
    ("Alora", 60, 30, 70)      
]

report(student_data)