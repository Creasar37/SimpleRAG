import os
from typing import List
from src.models.data_model import (VDBInitRequest, VDBInitResponse, VDBFileAddResponse, VDBListResponse, VDBDropRequest,
                                   VDBDropResponse, VDBFileListRequest, VDBFileListResponse, VDBFileDeleteRequest,
                                   VDBFileDeleteResponse)
from src.api.vdb.lancedb import lancedb_create, lancedb_insert, lancedb_delete, lancedb_file_delete
from src.api.vdb.milvus import milvus_create, milvus_insert, milvus_delete, milvus_file_delete
from src.logger.logger import logger
from fastapi import File, UploadFile
from src.utils.sql_executor import execute_sql
from src.api.vdb.documents import get_embed_text
from src.utils.utils import generate_file_hash


def vdb_init(init_request: VDBInitRequest):
    embedding_model = init_request.embedding_model
    vdb_name = init_request.vdb_name
    vdb_type = init_request.vdb_type
    params = init_request.params
    logger.info(f"开始创建向量库{vdb_name}")
    if vdb_type == "milvus":
        milvus_create(embedding_model, vdb_name, params)
    elif vdb_type == "lancedb":
        lancedb_create(embedding_model, vdb_name, params)
    else:
        raise Exception("vdb_type错误")
    return VDBInitResponse(status="success")


def add_file(vdb_name: str, files: List[UploadFile] = File(...)):
    sql_res = execute_sql(
        query="SELECT type, embedding_model_name FROM vdb_info WHERE name = ?;",
        params=(vdb_name, ),
        fetch_results=True
    )
    if not sql_res:
        raise Exception("vdb_name错误")
    vdb_type = sql_res[0][0]
    embedding_model_name = sql_res[0][1]
    file_info = vdb_list_files(VDBFileListRequest(vdb_name=vdb_name)).file_info
    file_hashs = {i["file_hash"] for i in file_info}
    if not os.path.exists(f"files/{vdb_name}"):
        os.mkdir(f"files/{vdb_name}")
    file_paths = []
    for file in files:
        file_path = f"files/{vdb_name}/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        file_hash = generate_file_hash(file_path)
        if file_hash in file_hashs:
            logger.info(f"文件{file.filename}已存在")
            continue
        file_paths.append(file_path)
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
        raise Exception("vdb_name错误")
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
    file_hashs = [row[0] for row in sql_res]
    sql_res = execute_sql(
        query="SELECT type FROM vdb_info WHERE name = ?;",
        params=(vdb_name, ),
        fetch_results=True
    )
    if not sql_res:
        raise Exception("vdb_name错误")
    vdb_type = sql_res[0][0]
    if vdb_type == "milvus":
        res = milvus_file_delete(vdb_name, file_hashs)
    elif vdb_type == "lancedb":
        res = lancedb_file_delete(vdb_name, file_hashs)
    else:
        raise Exception("vdb_type错误")
    if res:
        res = f"成功删除{res["delete_count"]}条"
        logger.info(res)
    else:
        res = ""
    return VDBFileDeleteResponse(status="success", details=res)
