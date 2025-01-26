# ✨ SimpleRAG

一个基于RAG的简易实现，包含FastAPI后端和Gradio前端。

## 🚀 功能特性

- **📚 向量库管理**:
  - ✔️ 创建/删除向量库（支持Milvus和LanceDB）
  - ✔️ 支持向量库索引等参数，参数通过sqlite数据库进行持久化
  - 📁 文件上传与管理，通过sqlite保存文件哈希值确保文件不重复
  - ⚡ 嵌入时通过本地缓存和redis缓存加快速度

- **⚙️ 检索配置**:
  - 🎯 支持top_k等参数调整
  - 🔄 可选检索重排功能

- **💬 LLM对话**:
  - 🤖 支持选择大模型并启用RAG增强

## 🛠️ 快速开始

### 安装依赖
```
# 一键安装所有依赖
pip install -r requirements.txt
```
> 📌 **提示**: Windows可能需要手动安装GPU版本torch

### 启动服务
```
# 启动后端API和前端界面
python start.py
```

- 🔗 后端API默认地址：`http://localhost:8320`
- 🌐 前端界面自动在浏览器打开：`http://localhost:8321`

## 🔧 配置参数
可在`conf/config.yaml`中修改：

## ❓ 常见问题

1. **🐢 LLM对话速度慢**  
   → 如日志提示`当前LLM加载设备为CPU，生成速度会比较慢`：  
   - 检查GPU可用性
   - 确认PyTorch是否正确安装GPU版本

2. **🆕 添加/更换模型**  
   - 📌 需要在`conf/config.yaml`加入模型参数
   - 🔧 嵌入模型仅支持sentence-transformers加载的模型，其他模型需修改`src/client/embedding.py`代码
   - 💻 LLM可通过在`src/client/LLM.py`添加对应类来添加
   - 🚀 项目启动时自动加载配置中的模型

## 📜 许可证
[MIT License](LICENSE)
