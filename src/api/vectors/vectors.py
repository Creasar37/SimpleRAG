from src.models.data_model import VectorsInitRequest, VectorsInitResponse
from src.api.vectors.lancedb import lancedb_create
from src.api.vectors.milvus import milvus_create
from src.logger.logger import logger


def vectors_init(init_request: VectorsInitRequest):
    embedding_model = init_request.embedding_model
    vectors_name = init_request.vectors_name
    vectors_type = init_request.vectors_type
    params = init_request.params
    logger.info(f"开始创建向量库{vectors_name}")
    if vectors_type == "milvus":
        milvus_create(embedding_model, vectors_name, params)
    elif vectors_type == "lancedb":
        lancedb_create(embedding_model, vectors_name, params)
    else:
        raise Exception("vectors_type错误")
    return VectorsInitResponse(status="success")
