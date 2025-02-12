import gradio as gr
from conf.config import config
from src.web_ui.req import chat_request, list_vdb, create_vdb, add_file, drop_vdb, file_list, file_delete


with gr.Blocks() as app:
    gr.Markdown("SimpleRAG")
    with gr.Tab("LLM对话"):
        llm_name = gr.Dropdown(choices=list(config["LLM"].keys()), label="选择大模型", interactive=True)
        use_rag = gr.Checkbox(label="使用RAG", value=True)
        with gr.Group() as rag_group:
            with gr.Row():
                vdb_name_chat = gr.Dropdown(choices=[], label="选择向量库", interactive=True, scale=4)
                app.load(
                    fn=lambda: gr.update(choices=list_vdb()),
                    inputs=None,
                    outputs=vdb_name_chat
                )
                vdb_name_chat_update_button = gr.Button(value="刷新")
                vdb_name_chat_update_button.click(
                    fn=lambda: gr.update(choices=list_vdb()),
                    inputs=None,
                    outputs=vdb_name_chat
                )
                top_k = gr.Slider(label="top_k", minimum=1, maximum=10, value=5, step=1, scale=5)
            use_rerank = gr.Checkbox(label="检索重排", value=False)
            with gr.Row(visible=False) as rerank_row:
                reranker = gr.Dropdown(choices=list(config["embedding_model"].keys()), label="选择重排模型", interactive=True)
                rerank_metric = gr.Textbox(label="重排评估指标", placeholder="请输入重排评估指标", value="cosine")
                rerank_top_k = gr.Slider(label="重排top_k", minimum=1, maximum=10, value=5, step=1)
            use_rerank.change(
                fn=lambda x: gr.update(visible=x),
                inputs=use_rerank,
                outputs=rerank_row
            )
            params_chat = gr.Textbox(label="其他参数", placeholder="请输入参数，json格式")
        use_rag.change(
            fn=lambda x: gr.update(visible=x),
            inputs=use_rag,
            outputs=rag_group
        )
        chat_history = gr.Chatbot(label="聊天记录", type="messages")
        query = gr.Textbox(label="输入框", placeholder="请输入问题")
        clear = gr.ClearButton([chat_history, query])
        query.submit(
            chat_request,
            inputs=[
                use_rag, vdb_name_chat, top_k, use_rerank, reranker, rerank_metric, rerank_top_k, params_chat,
                query, chat_history, llm_name
            ],
            outputs=[query, chat_history]
        )
    with gr.Tab("向量库管理"):
        with gr.Row():
            vdb_name = gr.Dropdown(choices=[], label="选择向量库", interactive=True, scale=8)
            app.load(
                fn=lambda: gr.update(choices=list_vdb()),
                inputs=None,
                outputs=vdb_name
            )
            with gr.Column(min_width=0):
                update_button = gr.Button(value="刷新")
                create_button = gr.Button(value="创建向量库")
            with gr.Column(min_width=0):
                drop_button = gr.Button(value="删除向量库")
                drop_confirm_button = gr.Button(value="确认删除", visible=False)
        drop_res = gr.Textbox(label="删除结果", visible=False, interactive=False)
        with gr.Group(visible=False) as create_group:
            with gr.Row():
                embedding_model = gr.Dropdown(
                    choices=list(config["embedding_model"].keys()), label="选择embedding_model", interactive=True
                )
                vdb_name_create = gr.Textbox(label="向量库名称", placeholder="请输入向量库名称")
                vdb_type = gr.Dropdown(choices=["milvus", "lancedb"], label="选择向量库类型", interactive=True)
            with gr.Row():
                params_create = gr.Textbox(label="其他参数", placeholder="请输入参数，json格式", scale=20)
            create_res = gr.Textbox(label="创建结果", visible=False, interactive=False)
            with gr.Row():
                real_create_button = gr.Button(value="创建", scale=9)
                create_hide_button = gr.Button(value="隐藏", min_width=0)
            real_create_button.click(
                fn=lambda: gr.update(visible=True),
                inputs=None,
                outputs=create_res
            ).then(
                create_vdb,
                inputs=[embedding_model, vdb_name_create, vdb_type, params_create],
                outputs=create_res
            )
            create_hide_button.click(
                fn=lambda: gr.update(visible=False),
                inputs=None,
                outputs=create_group
            )
        update_button.click(
            fn=lambda: gr.update(choices=list_vdb()),
            inputs=None,
            outputs=vdb_name
        )
        create_button.click(
            fn=lambda: gr.update(visible=True),
            inputs=None,
            outputs=create_group
        )
        drop_button.click(
            fn=lambda: gr.update(visible=True),
            inputs=None,
            outputs=drop_confirm_button
        ).then(
            fn=lambda: gr.update(visible=True),
            inputs=None,
            outputs=drop_res
        )
        drop_confirm_button.click(
            fn=lambda: gr.update(visible=False),
            inputs=None,
            outputs=drop_confirm_button
        ).then(
            fn=drop_vdb,
            inputs=vdb_name,
            outputs=drop_res
        )
        files = gr.File(label="上传文件", file_count="multiple")
        add_button = gr.Button(value="上传文件")
        add_res = gr.Textbox(label="上传结果", visible=False, interactive=False)
        add_button.click(
            fn=lambda: gr.update(visible=True),
            inputs=None,
            outputs=add_res
        ).then(
            add_file,
            inputs=[vdb_name, files],
            outputs=add_res
        )
        with gr.Row():
            file_name = gr.Dropdown(choices=[], label="选择文件名", interactive=True, multiselect=True, scale=9)
            app.load(
                fn=lambda x: gr.update(choices=file_list(x)),
                inputs=vdb_name,
                outputs=file_name
            )
            with gr.Column(min_width=0):
                update_file_list_button = gr.Button(value="刷新")
                delete_button = gr.Button(value="删除文件")
        delete_res = gr.Textbox(label="删除结果", visible=False, interactive=False)
        update_file_list_button.click(
            fn=lambda x: gr.update(choices=file_list(x)),
            inputs=vdb_name,
            outputs=file_name
        )
        delete_button.click(
            fn=lambda: gr.update(visible=True),
            inputs=None,
            outputs=delete_res
        ).then(
            file_delete,
            inputs=[vdb_name, file_name],
            outputs=delete_res
        )

if __name__ == "__main__":
    app.launch(
        server_name=config["server"]["web_ui"]["host"], server_port=config["server"]["web_ui"]["port"], inbrowser=True
    )
