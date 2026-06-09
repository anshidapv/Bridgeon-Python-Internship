from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext
import sqlite3
app = FastAPI()
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)
class userregister(BaseModel):
    email: str
    password: str
def get_connection():
    conn = sqlite3.connect("app.db")
    conn.row_factory = sqlite3.Row
    return conn
def init_db():
    conn = get_connection()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()
init_db()
@app.post("/auth/register")
def register(user: userregister):
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
    hashed_password = pwd_context.hash(
        user.password
    )
    conn.execute(
        """
        INSERT INTO 
    users(email,hashed_password)
        VALUES(?,?)
        """,
        (user.email,hashed_password)
    )
    conn.commit()
    conn.close()
    return{
        "message": "user registered successfully"
    }
@app.get("/users")
def get_users():
    conn = get_connection()
    users = conn.execute(
        "SELECT*FROM users"
    ).fetchall()
    conn.close()
    return [dict(user) for user in users]