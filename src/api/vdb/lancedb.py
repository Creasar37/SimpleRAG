import lancedb
import pyarrow as pa
from src.utils.sql_executor import execute_sql
from src.logger.logger import logger
from conf.config import config
import uuid


db = lancedb.connect("database/lancedb")


def lancedb_create(embedding_model, vdb_name):
    embeddings_dim = config["embedding_model"][embedding_model]["dim"]
    schema = pa.schema(
        [
            pa.field("id", pa.string(), nullable=False),
            pa.field("text", pa.string(), nullable=False),
            pa.field("file_hash", pa.string(), nullable=False),
            pa.field("embeddings", pa.list_(pa.float32(), embeddings_dim), nullable=False)
        ]
    )
    db.create_table(vdb_name, schema=schema)
    tbl = db.open_table(vdb_name)
    execute_sql(
        query="INSERT INTO vdb_info (name, type, embedding_model_name) VALUES (?, ?, ?);",
        params=(vdb_name, "lancedb", embedding_model)
    )
    logger.info(f"lancedb向量库{vdb_name}创建成功")


def lancedb_insert(vdb_name, texts, hashes, embeddings):
    tbl = db.open_table(vdb_name)
    data = [
        {
            "id": str(uuid.uuid1()),
            "text": texts[i],
            "file_hash": hashes[i],
            "embeddings": embeddings[i].tolist()
        }
        for i in range(len(texts))
    ]
    tbl.add(data)
    logger.info(f"lancedb向量库{vdb_name}插入成功")


def lancedb_delete(vdb_name):
    db.drop_table(vdb_name)
    execute_sql(
        query="DELETE FROM vdb_info WHERE name = ?;",
        params=(vdb_name, )
    )
    logger.info(f"lancedb向量库{vdb_name}删除成功")


def lancedb_file_delete(vdb_name, file_hashes):
    tbl = db.open_table(vdb_name)
    file_hashes = ", ".join([f"'{file_hash}'" for file_hash in file_hashes])
    tbl.delete(f"file_hash IN ({file_hashes})")
    logger.info(f"lancedb向量库{vdb_name}文件删除成功")


def lancedb_search(vdb_name, vector, top_k, params):
    metric_type = params["metric_type"]
    tbl = db.open_table(vdb_name)
    res = tbl.search(vector).select(["text"]).metric(metric_type).limit(top_k).to_list()
    # 距离越小越好
    res = [
        {
            "text": i["text"],
            "distance": i["_distance"]
        }
        for i in res
        if i["_distance"] < 0.8
    ]
    return res
