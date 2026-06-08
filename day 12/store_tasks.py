from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
app = FastAPI()
database_name = "app.db"
def init_db():
    conn = sqlite3.connect(database_name)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        completed BOOLEAN DEFAULT 0
    )
    """)
    conn.commit()
    conn.close()
@app.on_event("startup")
def startup():
    init_db()
class taskcreate(BaseModel):
    title: str
class taskresponse(BaseModel):
    id: int
    title: str
    completed: bool
@app.post("/tasks",
response_model=taskresponse)
def create_task(task: taskcreate):
    conn = sqlite3.connect(database_name)
    conn.row_factory= sqlite3.Row
    cursor = conn.execute(
        "INSERT INTO tasks(title)" \
        "VALUES(?)",
    (task.title,)
    ).fetchone()
    conn.close()
    return dict(row)
@app.get("/tasks",
response_model=list[taskresponse])
def get_tasks():
    conn = sqlite3.connect(database_name)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
    "SELECT*FROM tasks"
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]

