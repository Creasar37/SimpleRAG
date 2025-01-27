from fastapi import FastAPI
import os
from src.init.download import download_hf_model
from conf.config import config
from src.init.sql_init import create_sql_table
from src.client.embedding import EmbeddingClient
from src.client.llm import QwenClient


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


# 表初始化
create_sql_table("database/sqlite.db")

EmbedClient = EmbeddingClient()
QwenChatClient = QwenClient("Qwen2.5-0.5B-Instruct")
LLM = {
    "Qwen2.5-0.5B-Instruct": QwenChatClient
}