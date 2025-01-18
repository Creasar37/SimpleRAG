import redis
from conf.config import config


redis_client = redis.Redis(**config["Redis"])
