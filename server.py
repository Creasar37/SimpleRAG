from fastapi import FastAPI
from src.models.data_model import HealthCheckResponse

app = FastAPI()

app.get("/v1/healthcheck", response_model=HealthCheckResponse, summary="检查服务是否正常")(healthcheck)
