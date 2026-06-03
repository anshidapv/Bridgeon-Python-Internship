def calculate_grade( name: str, marks : list[int]) -> str:
    avg = sum(marks) / len(marks)
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"
grade= calculate_grade("alia", [73, 81, 65])
print("grade:", grade)
print("name:", "alia")
