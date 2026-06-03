#def greet(name):
#     return f"hello,{name}
def calculate_grade(*marks):
    avg= sum(marks) / len(marks)
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else: 
        return "F"
    return marks

# print(calculate_grade(65,73,81))