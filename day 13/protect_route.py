from fastapi import FastAPI,HTTPException,Header, Depends
from pydantic import BaseModel
from passlib.context import CryptContext
import sqlite3
import uuid
app = FastAPI()
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)
sessions={}
class userregister(BaseModel):
    email:str
    password:str
class userlogin(BaseModel):
    email:str
    password:str
class taskcreate(BaseModel):
    title:str
def get_connection():
    conn = sqlite3.connect("app.db")
    conn.row_factory = sqlite3.Row
    return conn
def init_db():
    conn = get_connection()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        hashed_password TEXT NOT NULL
    )
    """)
    conn.execute(""" 
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        owner_email TEXT
    )
    """)
    conn.commit()
    conn.close()
init_db()
@app.post("/auth/register")
def reqister(user: userregister):
    conn = get_connection()
    existing_user = conn.execute(
        "SELECT * FROM users WHERE email = ?",
        (user.email,)
    ).fetchone()
    if existing_user:
        conn.close()
        raise HTTPException(
            status_code=400,
            detail="email already exists"
        )
    hashed_password = user.pasword
    conn.execute(
        """
    INSERT INTO users(email,hashed_password)
    VALUES(?,?)
    """,
        (user.email, hashed_password)
    )
    conn.commit()
    conn.close()
    return {
        "message": "user registered successfully"
    }
@app.post("/auth/login")
def login(user: userlogin):
    conn = get_connection()
    db_user = conn.execute(
        "SELECT * FROM users WHERE email = ?",
        (user.email,)
    ).fetchone()
    conn.close()
    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    if user.password != db_user["hashed_password"]:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    token = str(uuid.uuid4())
    sessions[token] = user.email
    return {
        "token": token
    }
def get_current_user(
    authorization: str = Header(None)
):
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Missing token"
        )
    token = authorization.replace(
        "Bearer ",
        ""
    )
    if token not in sessions:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    return sessions[token]
@app.post("/tasks")
def create_task(
    task: taskcreate,
    user=Depends(get_current_user)
):
    conn = get_connection()
    conn.execute(
        """
        INSERT INTO tasks(title, owner_email)
        VALUES (?, ?)
        """,
        (task.title, user)
    )
    conn.commit()
    conn.close()
    return {
        "message": "Task created"
    }
@app.get("/tasks")
def get_tasks(
    user=Depends(get_current_user)
):
    conn = get_connection()
    tasks = conn.execute(
        """
        SELECT * FROM tasks
        WHERE owner_email = ?
        """,
        (user,)
    ).fetchall()
    conn.close()
    return [dict(task) for task in tasks]