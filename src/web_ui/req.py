import requests
import json
import gradio as gr
import os
from conf.config import config


base_url = f"http://{config["server"]["fastapi"]["host"]}:{config["server"]["fastapi"]["port"]}"


def chat_request(use_rag, vdb_name, top_k, use_rerank, reranker, rerank_metric, rerank_top_k, params,
                 msg, history, llm):
    if params == "":
        params = "{}"
    params = json.loads(params)
    data = {
        "query": msg,
        "llm": llm,
        "use_rag": use_rag,
        "vdb_name": vdb_name,
        "top_k": top_k,
        "use_rerank": use_rerank,
        "reranker": reranker,
        "rerank_metric": rerank_metric,
        "rerank_top_k": rerank_top_k,
        "params": params
    }
    ans = requests.post(f"{base_url}/v1/llm/chat", json=data).json()
    if not ans["details"]:
        ans = ans["answer"]
    else:
        ans = ans["details"]
    history.extend(
        [
            {"role": "user", "content": msg},
            {"role": "assistant", "content": ans}
        ]
    )
    return "", history


def list_vdb():
    ans = requests.get(f"{base_url}/v1/vdb/list").json()["vdb_name"]
    return ans


def create_vdb(embedding_model, vdb_name, vdb_type, params):
    if params == "":
        params = "{}"
    params = json.loads(params)
    data = {
        "embedding_model": embedding_model,
        "vdb_name": vdb_name,
        "vdb_type": vdb_type,
        "params": params
    }
    res = requests.post(f"{base_url}/v1/vdb/init", json=data).json()
    return "，".join([res["status"], res["details"]])


def add_file(vdb_name, files):
    file_objects = []
    file_data = []
    for path in files:
        f = open(path, "rb")
        file_objects.append(f)
        file_data.append(("files", (os.path.basename(path), f)))
    res = requests.post(f"{base_url}/v1/vdb/file/add", data={"vdb_name": vdb_name}, files=file_data).json()
    for f in file_objects:
        f.close()
    return "，".join([res["status"], res["details"]])


def drop_vdb(vdb_name):
    res = requests.post(f"{base_url}/v1/vdb/drop", json={"vdb_name": vdb_name}).json()
    return "，".join([res["status"], res["details"]])


def file_list(vdb_name):
    if not vdb_name:
        return []
    res = requests.post(f"{base_url}/v1/vdb/file/list", json={"vdb_name": vdb_name}).json()
    return [i["file_name"] for i in res["file_info"]]


def file_delete(vdb_name, file_name):
    res = requests.post(f"{base_url}/v1/vdb/file/delete", json={"vdb_name": vdb_name, "file_name": file_name}).json()
    return "，".join([res["status"], res["details"]])
