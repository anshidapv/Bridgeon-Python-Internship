from fastapi import APIRouter, HTTPException, Header
from passlib.context import CryptContext
from schemas import UserRegister, UserLogin
from database import get_connection
import uuid
router = APIRouter()
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)
sessions = {}
@router.post("/auth/register")
def register(user: UserRegister):
    conn = get_connection()
    existing = conn.execute(
        "SELECT * FROM users WHERE email=?",
        (user.email,)
    ).fetchone()
    if existing:
        conn.close()
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )
    hashed_password = pwd_context.hash(user.password)
    conn.execute(
        """
        INSERT INTO users(email, hashed_password)
        VALUES(?,?)
        """,
        (user.email, hashed_password)
    )
    conn.commit()
    conn.close()
    return {"message": "User registered"}
@router.post("/auth/login")
def login(user: UserLogin):
    conn = get_connection()
    db_user = conn.execute(
        "SELECT * FROM users WHERE email=?",
        (user.email,)
    ).fetchone()
    conn.close()
    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    if not pwd_context.verify(
        user.password,
        db_user["hashed_password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    token = str(uuid.uuid4())
    sessions[token] = user.email
    return {"access_token": token}
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
@router.get("/auth/me")
def me(
    user=Header(None),
    authorization: str = Header(None)
):
    email = get_current_user(authorization)
    return {"email": email}