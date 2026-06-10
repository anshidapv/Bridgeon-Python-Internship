from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from database import init_db
from auth import router as auth_router
load_dotenv()
app = FastAPI(
    title=os.getenv("APP_NAME")
)
init_db()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
@app.middleware("http")
async def log_requests(
    request: Request,
    call_next
):
    print(
        f"{request.method} {request.url}"
    )
    response = await call_next(request)
    return response
app.include_router(auth_router)
       
    