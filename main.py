from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database import engine, Base
from contextlib import asynccontextmanager
from routers import posts, users
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import func
from auth import create_access_token, hash_password, oauth2_scheme, verify_access_token, verify_password
from config import settings

@asynccontextmanager
async def lifespan(_app: FastAPI):
    # Startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Shutdown
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

app.include_router(posts.router, prefix="/posts", tags=["posts"])
app.include_router(users.router, prefix="/users", tags=["users"])

app.mount("/media", StaticFiles(directory="media"), name="media")
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/")
async def root():
    return {"message": "Hello World"}

