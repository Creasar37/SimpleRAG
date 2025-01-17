from src.init.init import app
from src.models.data_model import (HealthCheckResponse, VDBListResponse, VDBInitResponse, VDBAddResponse,
                                   VDBDropResponse)
from src.api.utils import healthcheck
from src.api.vdb.vdb import vdb_init, add_file, vdb_list_all, vdb_drop


app.get("/v1/healthcheck", response_model=HealthCheckResponse, summary="检查服务是否正常")(healthcheck)
app.get("/v1/vdb/list", response_model=VDBListResponse, summary="获取向量库列表")(vdb_list_all)
app.post("/v1/vdb/init", response_model=VDBInitResponse, summary="创建向量库")(vdb_init)
app.post("/v1/vdb/file/add", response_model=VDBAddResponse, summary="向量库文件上传")(add_file)
app.post("/v1/vdb/drop", response_model=VDBDropResponse, summary="删除向量库")(vdb_drop)

