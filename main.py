from fastapi import FastAPI
from contextlib import asynccontextmanager
from database.db_connection import init_db
import uvicorn
from views.user_view import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()  # ✅ Now properly initializes DB
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(user_router, prefix="/api/v1")


