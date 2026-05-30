class employee:
    def __init__(self,name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary
    def get_info(self):
        return f"{self.name} works in {self.department} and earns {self.salary}"
    def __str__(self):
        return f"employee: {self.name} ({self.department})"
emp = employee("alice","engineering",95000)
print(emp.get_info())
print(emp)