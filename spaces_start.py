from start import run_backend
from src.utils.utils import fastapi_test
from web_ui import app
from conf.config import config


if __name__ == "__main__":
    run_backend()
    fastapi_test(f"http://{config["server"]["fastapi"]["host"]}:{config["server"]["fastapi"]["port"]}")
    app.launch()
