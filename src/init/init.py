from fastapi import FastAPI
import os
import sqlite3
from src.init.sql_init import create_vectors_info_table

app = FastAPI()

if not os.path.exists("database"):
    os.mkdir("database")

conn = sqlite3.connect("database/sqlite.db")

# 表初始化
create_vectors_info_table("database/sqlite.db")
