import os
from typing import List
from src.models.data_model import (VDBInitRequest, VDBInitResponse, VDBFileAddResponse, VDBListResponse, VDBDropRequest,
                                   VDBDropResponse, VDBFileListRequest, VDBFileListResponse, VDBFileDeleteRequest,
                                   VDBFileDeleteResponse, LLMChatRequest, LLMChatResponse)
from src.api.vdb.lancedb import lancedb_create, lancedb_insert, lancedb_delete, lancedb_file_delete, lancedb_search
from src.api.vdb.milvus import milvus_create, milvus_insert, milvus_delete, milvus_file_delete, milvus_search
from src.logger.logger import logger
from fastapi import File, UploadFile, Form
from src.utils.sql_executor import execute_sql
from src.api.vdb.documents import get_embed_text
from src.utils.utils import generate_file_hash
from src.init.init import QwenChatClient
from conf.config import config
import json


def vdb_init(init_request: VDBInitRequest):
    embedding_model = init_request.embedding_model
    vdb_name = init_request.vdb_name
    vdb_type = init_request.vdb_type
    params = init_request.params
    logger.info(f"开始创建向量库{vdb_name}")
    sel_res = execute_sql(
        query="SELECT * FROM vdb_info WHERE name = ?;",
        params=(vdb_name, ),
        fetch_results=True
    )
    if sel_res:
        logger.info(f"向量库 {vdb_name} 已存在")
        return VDBInitResponse(status="error", details="向量库已存在")
    if vdb_type == "milvus":
        milvus_create(embedding_model, vdb_name, params)
    elif vdb_type == "lancedb":
        lancedb_create(embedding_model, vdb_name)
    else:
        return VDBInitResponse(status="error", details="vdb_type错误")
    return VDBInitResponse(status="success")


def add_file(vdb_name: str = Form(...), files: List[UploadFile] = File(...)):
    sql_res = execute_sql(
        query="SELECT type, embedding_model_name FROM vdb_info WHERE name = ?;",
        params=(vdb_name, ),
        fetch_results=True
    )
    if not sql_res:
        return VDBInitResponse(status="error", details="向量库不存在")
    vdb_type = sql_res[0][0]
    embedding_model_name = sql_res[0][1]
    file_info = vdb_list_files(VDBFileListRequest(vdb_name=vdb_name)).file_info
    file_hashes = {i["file_hash"] for i in file_info}
    if not os.path.exists(f"files/{vdb_name}"):
        os.mkdir(f"files/{vdb_name}")
    file_paths = []
    for file in files:
        file_path = f"files/{vdb_name}/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        file_hash = generate_file_hash(file_path)
        if file_hash in file_hashes:
            logger.info(f"文件{file.filename}已存在")
            continue
        file_paths.append(file_path)
    if not file_paths:
        return VDBFileAddResponse(status="success", details="全部文件已存在")
    texts, hashes, embeddings = get_embed_text(files=file_paths, embedding_model_name=embedding_model_name)
    if vdb_type == "milvus":
        res = milvus_insert(vdb_name, texts, hashes, embeddings)
    elif vdb_type == "lancedb":
        res = lancedb_insert(vdb_name, texts, hashes, embeddings)
    else:
        raise Exception("vdb_type错误")
    for path in file_paths:
        file_hash = generate_file_hash(path)
        execute_sql(
            query="INSERT OR IGNORE INTO files (file_hash, filename) VALUES (?, ?);",
            params=(file_hash, os.path.basename(path))
        )
        execute_sql(
            query="INSERT INTO file_vdb (file_hash, vdb_name) VALUES (?, ?)",
            params=(file_hash, vdb_name)
        )
    if res:
        res = f"成功插入{res["insert_count"]}条"
        logger.info(res)
    else:
        res = ""
    return VDBFileAddResponse(status="success", details=res)


def vdb_list_all():
    sql_res = execute_sql(
        query="SELECT name FROM vdb_info;",
        fetch_results=True
    )
    vdb_list = [sql_res[i][0] for i in range(len(sql_res))]
    return VDBListResponse(vdb_name=vdb_list)


def vdb_drop(drop_request: VDBDropRequest):
    vdb_name = drop_request.vdb_name
    sql_res = execute_sql(
        query="SELECT type FROM vdb_info WHERE name = ?;",
        params=(vdb_name, ),
        fetch_results=True
    )
    if not sql_res:
        return VDBDropResponse(status="error", details="向量库不存在")
    vdb_type = sql_res[0][0]
    if vdb_type == "milvus":
        milvus_delete(vdb_name)
    elif vdb_type == "lancedb":
        lancedb_delete(vdb_name)
    else:
        raise Exception("vdb_type错误")
    return VDBDropResponse(status="success")


def vdb_list_files(list_files_request: VDBFileListRequest):
    vdb_name = list_files_request.vdb_name
    sql_res = execute_sql(
        query="""
        SELECT files.file_hash, files.filename
        FROM files
        JOIN file_vdb ON files.file_hash = file_vdb.file_hash
        WHERE file_vdb.vdb_name = ?;
        """,
        params=(vdb_name, ),
        fetch_results=True
    )
    if not sql_res:
        file_info = []
    else:
        file_info = [{"file_hash": row[0], "file_name": row[1]} for row in sql_res]
    return VDBFileListResponse(file_info=file_info)


def file_delete(file_delete_request: VDBFileDeleteRequest):
    vdb_name = file_delete_request.vdb_name
    file_name = file_delete_request.file_name
    if isinstance(file_name, str):
        file_name = [file_name]
    placeholders = ", ".join("?" * len(file_name))
    sql_res = execute_sql(
        query=f"""
            SELECT file_hash
            FROM files
            WHERE filename IN ({placeholders});
        """,
        params=file_name,
        fetch_results=True
    )
    file_hashes = [row[0] for row in sql_res]
    sql_res = execute_sql(
        query="SELECT type FROM vdb_info WHERE name = ?;",
        params=(vdb_name, ),
        fetch_results=True
    )
    if not sql_res:
        return VDBFileDeleteResponse(status="error", details="向量库不存在")
    vdb_type = sql_res[0][0]
    if vdb_type == "milvus":
        res = milvus_file_delete(vdb_name, file_hashes)
    elif vdb_type == "lancedb":
        res = lancedb_file_delete(vdb_name, file_hashes)
    else:
        raise Exception("vdb_type错误")
    if res:
        res = f"成功删除{res["delete_count"]}条"
        logger.info(res)
    else:
        res = ""
    placeholders = ", ".join("?" * len(file_hashes))
    execute_sql(
        query=f"""
            DELETE FROM files
            WHERE file_hash IN ({placeholders});
        """,
        params=file_hashes
    )
    return VDBFileDeleteResponse(status="success", details=res)


def search(vdb_name, text, top_k, params):
    sql_res = execute_sql(
        query="SELECT type, embedding_model_name, parameters FROM vdb_info WHERE name = ?;",
        params=(vdb_name, ),
        fetch_results=True
    )
    if not sql_res:
        raise Exception("vdb_name错误")
    vdb_type = sql_res[0][0]
    embedding_model_name = sql_res[0][1]
    parameters = json.loads(sql_res[0][2]) if sql_res[0][2] else {}
    vector = get_embed_text(texts=text, embedding_model_name=embedding_model_name)[2]
    if vdb_type == "milvus":
        res = milvus_search(vdb_name, vector, top_k, parameters, params)
    elif vdb_type == "lancedb":
        if "metric_type" not in params:
            params["metric_type"] = config["LanceDB"]["default_metric_type"]
        res = lancedb_search(vdb_name, vector, top_k, params)
    else:
        raise Exception("vdb_type错误")
    return res


def llm_chat(chat_request: LLMChatRequest):
    query = chat_request.query
    use_rag = chat_request.use_rag
    vdb_name = chat_request.vdb_name
    top_k = chat_request.top_k
    params = chat_request.params
    if params is None:
        params = {}
    if use_rag:
        retrieval_res = search(vdb_name, query, top_k, params)
        logger.debug(retrieval_res)
        if not retrieval_res:
            return LLMChatResponse(answer="", details="向量库中未检索到")
        related_texts = "\n\n".join([i["text"] for i in retrieval_res])
        sys_prompt = config["Prompt"]["system"]["v1"]
        user_prompt = config["Prompt"]["user"]["v1"].format(text=related_texts, question=query)
        res = QwenChatClient(sys_prompt, user_prompt)
        return LLMChatResponse(answer=res)
    else:
        sys_prompt = config["Prompt"]["system"]["raw"]
        res = QwenChatClient(sys_prompt, query)
        return LLMChatResponse(answer=res)
