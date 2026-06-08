from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import(
    init_db,
    create_task,
    get_all_tasks,
    update_task,
    delete_task
)
app = FastAPI()
@app.on_event("startup")
def startup():
    init_db()
class taskcreate(BaseModel):
    title: str
class taskupdate(BaseModel):
    title: str
    completed: bool 
class taskresponse(BaseModel):
    id: int
    title: str
    completed: bool
@app.post("/tasks",
    response_model=taskresponse)
def add_task(task: taskcreate):
    return create_task(task.title)
@app.get("/tasks",
response_model=list[taskresponse])
def read_tasks():
    return get_all_tasks()
@app.put("/tasks/{task_id}")
def edit_task(task_id: int, task: taskupdate):
    updated = update_task(
        task_id,
        task.title,
        task.completed
    )
    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return updated
@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    deleted = delete_task(task_id)
    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return {"message": "Task deleted successfully"}
