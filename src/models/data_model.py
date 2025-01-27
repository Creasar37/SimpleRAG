from typing import List
from pydantic import BaseModel


class HealthCheckResponse(BaseModel):
    status: str
    details: dict = None


class VDBListResponse(BaseModel):
    vdb_name: List[str] = None


class VDBInitRequest(BaseModel):
    embedding_model: str = "bge-small-zh-v1.5"
    vdb_name: str = None
    vdb_type: str = "lancedb"
    params: dict = None


class VDBInitResponse(BaseModel):
    status: str
    details: str = ""


class VDBFileAddResponse(BaseModel):
    status: str
    details: str = ""


class VDBDropRequest(BaseModel):
    vdb_name: str = None


class VDBDropResponse(BaseModel):
    status: str
    details: str = ""


class VDBFileListRequest(BaseModel):
    vdb_name: str = None


class VDBFileListResponse(BaseModel):
    file_info: List[dict] = None


class VDBFileDeleteRequest(BaseModel):
    vdb_name: str = None
    file_name: List[str] | str = None


class VDBFileDeleteResponse(BaseModel):
    status: str
    details: str = ""


class LLMChatRequest(BaseModel):
    query: str = None
    llm: str = "Qwen2.5-0.5B-Instruct"
    stream: bool = False
    use_rag: bool = True
    vdb_name: str | None
    top_k: int = 5
    use_rerank: bool = False
    reranker: str = None
    rerank_metric: str = "cosine"
    rerank_top_k: int = 5
    params: dict = None


class LLMChatResponse(BaseModel):
    answer: str = None
    details: str = ""
