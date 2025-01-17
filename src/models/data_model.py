from typing import List
from pydantic import BaseModel

class HealthCheckResponse(BaseModel):
    status: str
    details: dict = None


class VectorsListResponse(BaseModel):
    vectors_name: List[str] = None


class VectorsInitRequest(BaseModel):
    embedding_model: str = "bge-small-zh-v1.5"
    vectors_name: str = None
    vectors_type: str = "lancedb"
    params: dict = None


class VectorsInitResponse(BaseModel):
    status: str
    details: dict = None


class VectorsAddResponse(BaseModel):
    status: str
    details: str = None


class VectorsDropResponse(BaseModel):
    status: str
    details: str = None
