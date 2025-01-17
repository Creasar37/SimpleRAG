from langchain_unstructured import UnstructuredLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.init.init import EmbedClient

def load_split(files):
    loader = UnstructuredLoader(files)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        separators=[
            "\n\n", "\n", " ", "。", "，", "、", "？", "！", "；", "：",
            ".", ",", "!", "?", ";", ":", "\u3000", "\u200b", ""
        ],
        chunk_size=500,
        chunk_overlap=50,
        length_function=len
    )
    text_list = []
    for doc in docs:
        splits = text_splitter.split_documents([doc])
        for split in splits:
            text_list.append(split.page_content)
    return text_list


def get_embed_text(files, embedding_model_name=None):
    texts = load_split(files)
    embeddings = EmbedClient.get_embedding(texts, embedding_model_name)
    return texts, embeddings
