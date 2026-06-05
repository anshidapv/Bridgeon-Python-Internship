from pydantic import BaseModel, ValidationError
class TaskModel(BaseModel):
    id: int
    title: str
def validate_task(data: dict):
    return TaskModel(**data)
try:
    task = validate_task({
        "id": 1,
        "title": "Learn Python"
    })
    print(task)
except ValidationError as e:
    print(e)
try:
    task = validate_task({
        "id": "abc",
        "title": "Learn Python"
    })
    print(task)
except ValidationError as e:
    print("Validation Error:")
    print(e)