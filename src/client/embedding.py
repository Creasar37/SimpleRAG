import pickle
from conf.config import config
from sentence_transformers import SentenceTransformer
from src.init.redis_init import redis_client
from src.logger.logger import logger


embedding_cache = {}


class EmbeddingClient:
    def __init__(self):
        self.model_names = list(config["embedding_model"].keys())
        self.models = {}
        logger.info("初始化embedding模型")
        for model_name in self.model_names:
            self.load_model(model_name)
        self.redis_retry = 0

    def load_model(self, model_name):
        self.models[model_name] = SentenceTransformer(config["embedding_model"][model_name]["path"])
        logger.info(f"加载模型：{model_name}")

    def get_embedding(self, texts, model_name=None):
        if model_name is None:
            model_name = "bge-small-zh-v1.5"
        if isinstance(texts, str):
            texts = [texts]
        embedding_keys = [f"embedding:{model_name}:{text}" for text in texts]
        embedding_list = []

        for i, key in enumerate(embedding_keys):
            if key in embedding_cache:
                embedding_list.append(embedding_cache[key])
            else:
                embedding_list.append(None)

        if self.redis_retry <= 3:
            try:
                missing_data = [(i, embedding_keys[i]) for i, embedding in enumerate(embedding_list) if embedding is None]
                if missing_data:
                    index_list, key_list = zip(*missing_data)
                    embeddings = redis_client.mget(key_list)
                    for i in range(len(key_list)):
                        if embeddings[i]:
                            embeddings_loaded = pickle.loads(embeddings[i])
                            embedding_list[index_list[i]] = embeddings_loaded
                            embedding_cache[key_list[i]] = embeddings_loaded
            except Exception as e:
                logger.warning(f"redis读取嵌入缓存失败：{e}")
                self.redis_retry += 1

        missing_data = [(i, embedding_keys[i], texts[i]) for i, embedding in enumerate(embedding_list) if embedding is None]
        if missing_data:
            index_list, key_list, text_list = zip(*missing_data)
            embeddings = self.models[model_name].encode(text_list, normalize_embeddings=True)
            for i in range(len(text_list)):
                embedding_list[index_list[i]] = embeddings[i]
                embedding_cache[key_list[i]] = embeddings[i]
                if self.redis_retry <= 3:
                    try:
                        redis_client.set(key_list[i], pickle.dumps(embeddings[i]), ex=60*60*24*7)
                    except Exception as e:
                        logger.warning(f"redis插入嵌入缓存失败：{e}")
                        self.redis_retry += 1
            # redis_client.mset({key_list[i]: pickle.dumps(embeddings[i]) for i in range(len(key_list))})
        if self.redis_retry > 3:
            logger.warning("redis重试次数过多，请检查redis连接")
        return embedding_list
