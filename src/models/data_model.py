from pydantic import BaseModel

class HealthCheckResponse(BaseModel):
    status: str
    details: dict = None

class VectorsInitRequest(BaseModel):
    embedding_model: str
    vectors_name: str
    vectors_type: str
    params: dict = None


class VectorsInitResponse(BaseModel):
    status: str
    details: dict = None
