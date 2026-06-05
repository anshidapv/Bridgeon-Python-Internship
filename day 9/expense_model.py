from pydantic import BaseModel, ValidationError
class Expense(BaseModel):
    title: str
    amount: float
    category: str
expenses: list[Expense] = []
def add_expense(data: dict) -> None:
    expense = Expense(**data)
    expenses.append(expense)
    print("Expense added successfully!")
def view_expenses() -> None:
    if not expenses:
        print("No expenses found.")
        return
    for expense in expenses:
        print(
            f"Title: {expense.title}, "
            f"Amount: {expense.amount}, "
            f"Category: {expense.category}"
        )
def calculate_total() -> float:
    return sum(expense.amount for expense in expenses)
def main() -> None:
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Exit")
        choice: str = input("Enter choice: ")
        if choice == "1":
            try:
                data = {
                    "title": input("Enter title: "),
                    "amount": float(input("Enter amount: ")),
                    "category": input("Enter category: ")
                }
                add_expense(data)
            except ValidationError as e:
                print("Validation Error:")
                print(e)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Total Expense:", calculate_total())
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
main()