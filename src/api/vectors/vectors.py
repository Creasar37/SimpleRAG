import os
from typing import List
from src.models.data_model import VectorsInitRequest, VectorsInitResponse, VectorsAddResponse, VectorsListResponse
from src.api.vectors.lancedb import lancedb_create, lancedb_insert, lancedb_delete
from src.api.vectors.milvus import milvus_create, milvus_insert, milvus_delete
from src.logger.logger import logger
from fastapi import File, UploadFile
from src.utils.sql_executor import execute_sql
from src.api.vectors.documents import get_embed_text


def vectors_init(init_request: VectorsInitRequest):
    embedding_model = init_request.embedding_model
    vectors_name = init_request.vectors_name
    vectors_type = init_request.vectors_type
    params = init_request.params
    logger.info(f"开始创建向量库{vectors_name}")
    if vectors_type in ["milvus", "milvus-lite"]:
        milvus_create(embedding_model, vectors_name, params)
    elif vectors_type == "lancedb":
        lancedb_create(embedding_model, vectors_name, params)
    else:
        raise Exception("vectors_type错误")
    return VectorsInitResponse(status="success")


def add_file(vectors_name: str, files: List[UploadFile] = File(...)):
    sql_res = execute_sql(
        query="SELECT type, embedding_model_name FROM vectors_info WHERE name = ?;",
        params=(vectors_name, ),
        fetch_results=True
    )
    if not sql_res:
        raise Exception("vectors_name错误")
    vectors_type = sql_res[0][0]
    embedding_model_name = sql_res[0][1]
    if not os.path.exists(f"files/{vectors_name}"):
        os.mkdir(f"files/{vectors_name}")
    file_paths = []
    for file in files:
        file_path = f"files/{vectors_name}/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
            file_paths.append(file_path)
    texts, embeddings = get_embed_text(file_paths, embedding_model_name)
    if vectors_type == "milvus":
        res = milvus_insert(vectors_name, texts, embeddings)
    elif vectors_type == "lancedb":
        res = lancedb_insert(vectors_name, texts, embeddings)
    else:
        raise Exception("vectors_type错误")
    if res:
        res = f"成功插入{res["insert_count"]}条"
        logger.info(res)
    return VectorsAddResponse(status="success", details=res)


def vectors_list_all():
    sql_res = execute_sql(
        query="SELECT name FROM vectors_info;",
        fetch_results=True
    )
    vectors_list = [sql_res[i][0] for i in range(len(sql_res))]
    return VectorsListResponse(vectors_name=vectors_list)


def vectors_delete(vectors_name: str):
    sql_res = execute_sql(
        query="SELECT type FROM vectors_info WHERE name = ?;",
        params=(vectors_name, ),
        fetch_results=True
    )
    if not sql_res:
        raise Exception("vectors_name错误")
    vectors_type = sql_res[0][0]
    if vectors_type == "milvus":
        milvus_delete(vectors_name)
    elif vectors_type == "lancedb":
        lancedb_delete(vectors_name)
    else:
        raise Exception("vectors_type错误")
