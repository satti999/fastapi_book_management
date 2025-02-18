import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str=os.getenv("DATABASE_URL")
    SECRET_KEY: str=os.getenv("SECRET_KEY")
    ALGORITHM: str=os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int=os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    REDIS_HOST = "localhost"  # Change if using Docker (e.g., "redis")
    REDIS_PORT = 6379
    REDIS_DB = 0
    REDIS_PASSWORD = None
    


settings = Settings()

   