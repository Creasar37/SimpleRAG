import lancedb
import pyarrow as pa
from src.utils.sql_executor import execute_sql
from src.logger.logger import logger
from conf.config import config
import uuid


db = lancedb.connect("database/lancedb")

def lancedb_create(embedding_model, vdb_name, params):
    sel_res = execute_sql(
        query="SELECT * FROM vdb_info WHERE name = ?;",
        params=(vdb_name, ),
        fetch_results=True
    )
    if sel_res:
        logger.info(f"向量库 {vdb_name} 已存在")
        raise Exception("向量库已存在")
    embeddings_dim = config["embedding_model"][embedding_model]["dim"]
    schema = pa.schema(
        [
            pa.field("id", pa.string(), nullable=False),
            pa.field("text", pa.string(), nullable=False),
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


def lancedb_insert(vdb_name, texts, embeddings):
    tbl = db.open_table(vdb_name)
    data = [
        {
            "id": str(uuid.uuid1()),
            "text": texts[i],
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
