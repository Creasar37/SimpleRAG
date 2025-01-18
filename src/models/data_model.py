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
    details: str = None


class VDBFileAddResponse(BaseModel):
    status: str
    details: str = None


class VDBDropRequest(BaseModel):
    vdb_name: str = None


class VDBDropResponse(BaseModel):
    status: str
    details: str = None


class VDBFileListRequest(BaseModel):
    vdb_name: str = None


class VDBFileListResponse(BaseModel):
    file_info: List[dict] = None
