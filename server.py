from src.init.init import app
from src.models.data_model import (HealthCheckResponse, VectorsListResponse, VectorsInitResponse, VectorsAddResponse,
                                   VectorsDropResponse)
from src.api.utils import healthcheck
from src.api.vectors.vectors import vectors_init, add_file, vectors_list_all, vectors_delete


app.get("/v1/healthcheck", response_model=HealthCheckResponse, summary="检查服务是否正常")(healthcheck)
app.get("/v1/vectors/list", response_model=VectorsListResponse, summary="获取向量库列表")(vectors_list_all)
app.post("/v1/vectors/init", response_model=VectorsInitResponse, summary="创建向量库")(vectors_init)
app.post("/v1/vectors/file/add", response_model=VectorsAddResponse, summary="向量库文件上传")(add_file)
app.post("/v1/vectors/del_base", response_model=VectorsDropResponse, summary="删除向量库")(vectors_delete)

