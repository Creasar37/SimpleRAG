from fastapi import FastAPI
import os
from src.init.sql_init import create_vectors_info_table
import redis
from conf.config import config

app = FastAPI()

if not os.path.exists("database"):
    os.mkdir("database")

# 表初始化
create_vectors_info_table("database/sqlite.db")

redis_client = redis.Redis(**config["Redis"])

