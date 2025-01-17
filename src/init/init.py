from fastapi import FastAPI
import os
from src.init.download import download_hf_model
from conf.config import config


models = {**config["embedding_model"], **config["LLM"]}
hf_name_list = [models[model]["hf_name"] for model in models]
model_path_list = [models[model]["path"] for model in models]

for i in range(len(hf_name_list)):
    if not os.path.exists(model_path_list[i]):
        download_hf_model(hf_name_list[i], model_path_list[i])


app = FastAPI()

if not os.path.exists("database"):
    os.mkdir("database")
if not os.path.exists("files"):
    os.mkdir("files")


from src.init.sql_init import create_vdb_info_table
from src.client.embedding import EmbeddingClient


# 表初始化
create_vdb_info_table("database/sqlite.db")

EmbedClient = EmbeddingClient()
