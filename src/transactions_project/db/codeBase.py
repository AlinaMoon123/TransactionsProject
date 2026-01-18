import redis.asyncio
from src.transactions_project.core.config import REDIS_HOST, REDIS_PORT

redis_client = redis.asyncio.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)
