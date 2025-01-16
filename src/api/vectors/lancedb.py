import lancedb
import pyarrow as pa
from src.utils.sql_executor import execute_sql
from src.logger.logger import logger
from conf.config import config

db = lancedb.connect("database/lancedb")

def lancedb_create(embedding_model, vectors_name, vector_type, params):
    sel_res = execute_sql(
        query="SELECT * FROM vectors_info WHERE name = ? AND type = ?;",
        params=(vectors_name, vector_type),
        fetch_results=True
    )
    if sel_res:
        logger.info(f"向量库 {vectors_name} 已存在")
        raise Exception("向量库已存在")
    embeddings_dim = config["embedding_model"][embedding_model]["dim"]
    if "index_type" in params:
        index_type = params["index_type"]
    else:
        index_type = config["LanceDB"]["default_index_type"]
    if "index_params" in params:
        index_params = params["index_params"]
    else:
        index_params = {}
    if "metric_type" in params:
        metric_type = params["metric_type"]
    else:
        metric_type = config["LanceDB"]["default_metric_type"]
    schema = pa.schema(
        [
            pa.field("id", pa.int64(), nullable=False),
            pa.field("text", pa.string(), nullable=False),
            pa.field("embeddings", pa.list_(pa.float32(), embeddings_dim), nullable=False)
        ]
    )
    db.create_table(vectors_name, schema=schema)
    tbl = db.open_table(vectors_name)
    execute_sql(
        query="INSERT INTO vectors_info (name, type, embedding_model_name) VALUES (?, ?, ?);",
        params=(vectors_name, "lancedb", embedding_model)
    )
    logger.info(f"lancedb向量库{vectors_name}创建成功")