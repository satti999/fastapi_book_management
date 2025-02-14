from typing import Union
from contextlib import asynccontextmanager
from database.db_connection import init_db
from fastapi import FastAPI



@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)