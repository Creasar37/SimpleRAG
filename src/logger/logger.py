import logging
import os
from logging.handlers import TimedRotatingFileHandler

# 创建日志文件夹（如果不存在）
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 定义日志文件路径
log_file = os.path.join(log_dir, "app.log")

# 配置日志格式
formatter = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S:%f"
)

# 创建 TimedRotatingFileHandler，按天分割日志文件
file_handler = TimedRotatingFileHandler(log_file, when="D", interval=1)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

# 创建 StreamHandler，用于输出到控制台
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

# 创建 Logger
logger = logging.getLogger("AppLogger")
logger.setLevel(logging.DEBUG)

# 避免重复添加处理器
if not logger.hasHandlers():
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


def get_logger(name: str):
    """
    获取一个带指定名称的 logger。
    :param name: str - logger 的名称（通常为调用者的模块名）
    :return: logging.Logger - 配置好的 logger 实例
    """
    return logger.getChild(name)
