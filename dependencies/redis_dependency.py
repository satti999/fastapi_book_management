import redis
from core.config import settings


redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    password=settings.REDIS_PASSWORD,
    decode_responses=True  # Ensures data is returned as strings
)

def get_redis():
    return redis_client
