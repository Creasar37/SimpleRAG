from src.init.init import app
from src.models.data_model import HealthCheckResponse
from src.api.utils import healthcheck


app.get("/v1/healthcheck", response_model=HealthCheckResponse, summary="检查服务是否正常")(healthcheck)
