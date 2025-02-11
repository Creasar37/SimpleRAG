from start import run_backend
from src.utils.utils import fastapi_test
from web_ui import app
from conf.config import config
import os


if __name__ == "__main__":
    retry_times = 30
    if "models" not in os.listdir():
        retry_times = 500
    run_backend()
    fastapi_test(f"http://{config["server"]["fastapi"]["host"]}:{config["server"]["fastapi"]["port"]}",
                 retry=retry_times)
    app.launch()
