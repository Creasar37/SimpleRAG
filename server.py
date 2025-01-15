from src.init.init import app
from src.models.data_model import HealthCheckResponse, VectorsInitResponse
from src.api.utils import healthcheck
from src.api.vectors.vectors import vectors_init


app.get("/v1/healthcheck", response_model=HealthCheckResponse, summary="检查服务是否正常")(healthcheck)
app.post("/v1/vectors/init", response_model=VectorsInitResponse, summary="创建向量库")(vectors_init)

