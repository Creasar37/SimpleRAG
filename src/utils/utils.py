import hashlib
import time
import requests


def generate_file_hash(file_path):
    """生成文件内容的哈希码（使用 SHA256）"""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def fastapi_test(base_url, retry=30):
    time.sleep(5)
    n = 0
    while n <= retry:
        try:
            requests.get(f"{base_url}/v1/healthcheck")
            break
        except Exception:
            time.sleep(5)
            n += 1
    else:
        raise Exception("FastAPI启动超时")
