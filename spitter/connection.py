import os
import redis

redis_url = os.getenv("REDIS_URL", "redis://127.0.0.1:6379")
redis_conn = redis.from_url(redis_url)
