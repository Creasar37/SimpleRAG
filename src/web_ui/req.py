import requests
import json
import gradio as gr
import os


base_url = "http://localhost:21235"


def chat_request(use_rag, vdb_name, top_k, params, msg, history):
    if params == "":
        params = "{}"
    params = json.loads(params)
    data = {
        "query": msg,
        "use_rag": use_rag,
        "vdb_name": vdb_name,
        "top_k": top_k,
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
    return gr.Dropdown(choices=ans, label="选择向量库", interactive=True, scale=9)


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
    res = requests.post(f"{base_url}/v1/vdb/file/list", json={"vdb_name": vdb_name}).json()
    return [i["file_name"] for i in res["file_info"]]


def file_delete(vdb_name, file_name):
    res = requests.post(f"{base_url}/v1/vdb/file/delete", json={"vdb_name": vdb_name, "file_name": file_name}).json()
    return "，".join([res["status"], res["details"]])
