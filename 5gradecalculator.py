class InvalidMarkError(Exception):
    pass


def calculate(name, *marks):

    if len(marks) == 0:
        raise InvalidMarkError("No marks entered")

    for mark in marks:
        if mark < 0 or mark > 100:
            raise InvalidMarkError("Invalid Mark")

    avg = sum(marks) / len(marks)

    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "F"

    return avg, grade


def report(students):

    print("Name\tAverage\tGrade")

    for student in students:

        name = student[0]
        marks = student[1:]

        try:
            avg, grade = calculate(name, *marks)
            print(f"{name}\t{avg:.2f}\t{grade}")

        except InvalidMarkError as e:
            print(f"{name}\tError: {e}")


students = [
    ("Anshida", 80, 90, 70),    
    ("Riya", 95, 92, 90),       
    ("Jerry", 150, 80, 70),     
    ("Zara",),                  
    ("Alora", 60, -10, 70)      
]

report(students)