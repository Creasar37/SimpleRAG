from src.init.init import app
from src.models.data_model import (HealthCheckResponse, VDBListResponse, VDBInitResponse, VDBFileAddResponse,
                                   VDBDropResponse, VDBFileListResponse, VDBFileDeleteResponse, LLMChatResponse)
from src.api.utils import healthcheck
from src.api.vdb.vdb import vdb_init, add_file, vdb_list_all, vdb_drop, vdb_list_files, file_delete, llm_chat


app.get("/v1/healthcheck", response_model=HealthCheckResponse, summary="检查服务是否正常")(healthcheck)
app.get("/v1/vdb/list", response_model=VDBListResponse, summary="获取向量库列表")(vdb_list_all)
app.post("/v1/vdb/init", response_model=VDBInitResponse, summary="创建向量库")(vdb_init)
app.post("/v1/vdb/file/add", response_model=VDBFileAddResponse, summary="向量库文件上传")(add_file)
app.post("/v1/vdb/drop", response_model=VDBDropResponse, summary="删除向量库")(vdb_drop)
app.post("/v1/vdb/file/list", response_model=VDBFileListResponse, summary="获取向量库文件列表")(vdb_list_files)
app.post("/v1/vdb/file/delete", response_model=VDBFileDeleteResponse, summary="删除向量库文件")(file_delete)
app.post("/v1/llm/chat", response_model=LLMChatResponse, summary="LLM对话")(llm_chat)
