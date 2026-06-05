from typing import Dict, List
class TaskNotFoundError(Exception):
    pass
class TaskAlreadyExistsError(Exception):
    pass
tasks: Dict[int, dict] = {}
def get_all_tasks() -> List[dict]:
    return list(tasks.values())
def get_task(id: int) -> dict:
    if id not in tasks:
        raise TaskNotFoundError(f"Task {id} not found")
    return tasks[id]
def create_task(data: dict) -> dict:
    task_id: int = data["id"]
    if task_id in tasks:
        raise TaskAlreadyExistsError(f"Task {task_id} already exists")
    tasks[task_id] = data
    return data
def update_task(id: int, data: dict) -> dict:
    if id not in tasks:
        raise TaskNotFoundError(f"Task {id} not found")
    tasks[id] = data
    return data
def delete_task(id: int) -> bool:
    if id not in tasks:
        raise TaskNotFoundError(f"Task {id} not found")
    del tasks[id]
    return True
def main() -> None:
    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Create Task")
        print("2. View All Tasks")
        print("3. View Task By ID")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")
        choice: str = input("Enter choice: ")
        try:
            if choice == "1":
                task_id: int = int(input("Enter ID: "))
                title: str = input("Enter Title: ")
                task = {
                    "id": task_id,
                    "title": title
                }
                print(create_task(task))
            elif choice == "2":
                print(get_all_tasks())
            elif choice == "3":
                task_id = int(input("Enter ID: "))
                print(get_task(task_id))
            elif choice == "4":
                task_id = int(input("Enter ID: "))
                title = input("Enter New Title: ")
                updated_task = {
                    "id": task_id,
                    "title": title
                }
                print(update_task(task_id, updated_task))
            elif choice == "5":
                task_id = int(input("Enter ID: "))
                delete_task(task_id)
                print("Task deleted successfully!")
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")
        except (TaskNotFoundError, TaskAlreadyExistsError) as e:
            print("Error:", e)
        except ValueError:
            print("Please enter a valid number.")
main()