
from redis import Redis
from core.config import settings

redis_client = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    decode_responses=True  # Ensures data is returned as strings
)

# from redis import Redis

# redis_client = Redis(host="localhost", port=6379, db=0)

def get_redis():
    return redis_client






