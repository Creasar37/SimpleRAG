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
        for model_name in self.model_names:
            self.load_model(model_name)
    def load_model(self, model_name):
        self.models[model_name] = SentenceTransformer(config["embedding_model"][model_name]["path"])
        logger.info(f"加载模型：{model_name}")
    def get_embedding(self, texts, model_name=None):
        if model_name is None:
            model_name = "bge-small-zh-v1.5"
        embedding_keys = [f"embedding:{model_name}:{text}" for text in texts]
        embedding_list = []

        for i, key in enumerate(embedding_keys):
            if key in embedding_cache:
                embedding_list.append(embedding_cache[key])
            else:
                embedding_list.append(None)

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

        missing_data = [(i, embedding_keys[i], texts[i]) for i, embedding in enumerate(embedding_list) if embedding is None]
        if missing_data:
            index_list, key_list, text_list = zip(*missing_data)
            embeddings = self.models[model_name].encode(text_list, normalize_embeddings=True)
            for i in range(len(text_list)):
                embedding_list[index_list[i]] = embeddings[i]
                embedding_cache[key_list[i]] = embeddings[i]
                redis_client.set(key_list[i], pickle.dumps(embeddings[i]), ex=60*60*24*7)
            # redis_client.mset({key_list[i]: pickle.dumps(embeddings[i]) for i in range(len(key_list))})

        return embedding_list
