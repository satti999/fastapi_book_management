from fastapi import FastAPI

from contextlib import asynccontextmanager
from database.db_connection import init_db
from views.user_view import router as user_router
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()  
    yield



app = FastAPI(lifespan=lifespan)

app.include_router(user_router, prefix="/api/v1/user")


