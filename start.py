import subprocess
import time
import sys


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
    run_backend()
    run_frontend()

    # 阻塞主进程
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n已终止服务")
