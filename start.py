import os
import subprocess
import time
import sys
from src.utils.utils import fastapi_test
from conf.config import config


def run_backend():
    """启动 FastAPI 后端"""
    subprocess.Popen(
        [sys.executable, "server.py"],
        stdout=sys.stdout,
        stderr=sys.stderr
    )


def run_frontend():
    """启动 Gradio 前端"""
    subprocess.Popen(
        [sys.executable, "web_ui.py"],
        stdout=sys.stdout,
        stderr=sys.stderr
    )


if __name__ == "__main__":
    retry_times = 30
    if "models" not in os.listdir():
        retry_times = 500
    run_backend()
    fastapi_test(f"http://{config['server']['fastapi']['host']}:{config['server']['fastapi']['port']}",
                 retry=retry_times)
    run_frontend()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("已终止服务")
