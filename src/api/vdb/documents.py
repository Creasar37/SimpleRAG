from langchain_unstructured import UnstructuredLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.init.init import EmbedClient
from src.utils.utils import generate_file_hash


def load_split(files):
    loader = UnstructuredLoader(files)
    docs = loader.load()
    hash_dict = {f"{file}": generate_file_hash(file) for file in files}
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
    hash_lists = []
    for doc in docs:
        splits = text_splitter.split_documents([doc])
        hash_item = hash_dict[doc.metadata["source"]]
        for split in splits:
            text_list.append(split.page_content)
            hash_lists.append(hash_item)
    return text_list, hash_lists


def get_embed_text(files, embedding_model_name=None):
    texts, hashes = load_split(files)
    embeddings = EmbedClient.get_embedding(texts, embedding_model_name)
    return texts, hashes, embeddings
