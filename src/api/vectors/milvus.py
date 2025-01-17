from pymilvus import MilvusClient, DataType
from conf.config import config
from src.logger.logger import logger
from src.utils.sql_executor import execute_sql
import json

client = MilvusClient("database/milvus.db")

def milvus_create(embedding_model, vectors_name, params):
    sel_res = execute_sql(
        query="SELECT * FROM vectors_info WHERE name = ?;",
        params=(vectors_name, ),
        fetch_results=True
    )
    if sel_res:
        logger.info(f"向量库 {vectors_name} 已存在")
        raise Exception("向量库已存在")
    embeddings_dim = config["embedding_model"][embedding_model]["dim"]
    if "index_type" in params:
        index_type = params["index_type"]
        index_params = config["Milvus"]["index_params"][index_type]
        for index_param in index_params:
            if index_param in params["index_params"]:
                index_params[index_param] = params["index_params"][index_param]
    else:
        index_type = config["Milvus"]["default_index_type"]
        index_params = {}
    if "metric_type" in params:
        metric_type = params["metric_type"]
    else:
        metric_type = config["Milvus"]["default_metric_type"]
    col_schema = MilvusClient.create_schema(auto_id=True)
    col_schema.add_field(field_name="id", datatype=DataType.INT64, is_primary=True)
    col_schema.add_field(field_name="text", datatype=DataType.VARCHAR, max_length=5000)
    col_schema.add_field(field_name="embeddings", datatype=DataType.FLOAT_VECTOR, dim=embeddings_dim)
    col_index_params = client.prepare_index_params()
    col_index_params.add_index(
        field_name="embeddings", index_type=index_type,
        metric_type=metric_type, params=index_params.copy()
    )
    client.create_collection(collection_name=vectors_name, schema=col_schema, index_params=col_index_params)
    all_params = {"index_type": index_type, "metric_type": metric_type, "index_params": index_params}
    execute_sql(
        query="INSERT INTO vectors_info (name, type, embedding_model_name, parameters) VALUES (?, ?, ?, ?);",
        params=(vectors_name, "milvus", embedding_model, json.dumps(all_params))
    )
    logger.info(f"milvus向量库{vectors_name}创建成功")


def milvus_insert(vectors_name, texts, embeddings):
    for i, text in enumerate(texts):
        if len(text) > 500:
            print(f"Row {i}: Text length {len(text)} exceeds max length 500")
    data = [
        {
            "text": texts[i],
            "embeddings": embeddings[i].tolist()
        }
        for i in range(len(texts))
    ]
    res = client.insert(collection_name=vectors_name, data=data)
    return res
