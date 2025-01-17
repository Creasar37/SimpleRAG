from fastapi import FastAPI
import os
from src.init.sql_init import create_vdb_info_table
from src.client.embedding import EmbeddingClient


app = FastAPI()

if not os.path.exists("database"):
    os.mkdir("database")
if not os.path.exists("files"):
    os.mkdir("files")

# 表初始化
create_vdb_info_table("database/sqlite.db")


EmbedClient = EmbeddingClient()
