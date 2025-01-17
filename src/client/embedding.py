from conf.config import config
from sentence_transformers import SentenceTransformer
from src.init.init import redis_client
from src.logger.logger import logger


embedding_cache = {}

class EmbeddingClient:
    def __init__(self):
        self.model_names = list(config.embedding_model.keys())
        self.models = {}
        for model_name in self.model_names:
            self.load_model(model_name)
    def load_model(self, model_name):
        self.models[model_name] = SentenceTransformer(config.embedding_model[model_name]["path"])
    def get_embedding(self, texts, model_name):
        embedding_keys = [f"embedding:{model_name}:{text}" for text in texts]
        embedding_list = []

        for i, key in enumerate(embedding_keys):
            if key in embedding_cache:
                embedding_list.append(embedding_cache[key])
            else:
                embedding_list.append(None)

        try:
            index_list, key_list = zip(*[(i, embedding_keys[i]) for i, embedding in enumerate(embedding_list) if embedding is None])
            if len(key_list) > 0:
                embeddings = redis_client.mget(key_list)
                for i in range(len(key_list)):
                    embedding_list[index_list[i]] = embeddings[i]
                    embedding_cache[key_list[i]] = embeddings[i]
        except Exception as e:
            logger.warning("redis读取嵌入缓存失败")

        index_list, key_list, text_list = zip(*[(i, embedding_keys[i], texts[i]) for i, embedding in enumerate(embedding_list) if embedding is None])
        if len(text_list) > 0:
            embeddings = self.models[model_name].encode(text_list, normalize_embeddings=True)
            for i in range(len(text_list)):
                embedding_list[index_list[i]] = embeddings[i]
                embedding_cache[key_list[i]] = embeddings[i]
            redis_client.mset({key_list[i]: embeddings[i] for i in range(len(key_list))})

        return embedding_list
