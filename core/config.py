import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from typing import Optional
from typing import ClassVar


load_dotenv(override=True)

class Settings(BaseSettings):
    DATABASE_URL: str=os.getenv("DATABASE_URL")
    SECRET_KEY: str=os.getenv("SECRET_KEY")
    ALGORITHM: str=os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int=os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    REDIS_HOST : str = "localhost" 
    REDIS_PORT : int = 6379
    REDIS_DB : int = 0
   


settings = Settings()

   