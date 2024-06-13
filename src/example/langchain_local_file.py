import pickle
from langchain_openai import OpenAIEmbeddings
from langchain.storage import InMemoryStore
from langchain.storage import LocalFileStore
from langchain.embeddings import CacheBackedEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma


# https://github.com/openai/openai-python/issues/676
# from openai.embeddings_utils import get_embedding, cosine_similarity
# from langchain.vectorstores import FAISS


def save_to_memory_store():
    flower_store = InMemoryStore()
    flower_embeddings = OpenAIEmbeddings()
    flower_embedder = CacheBackedEmbeddings.from_bytes_store(
        flower_embeddings,
        flower_store,
        namespace=flower_embeddings.model)
    embeddings = flower_embedder.embed_documents(["你好", "智能鲜花客服", "马王爷有6只眼"])
    print("共生成向量个数:", len(embeddings))
    flower_embedder.embed_query("马王爷有几只眼？")


def save_to_local_file():
    cached_embedder = CacheBackedEmbeddings.from_bytes_store(
        OpenAIEmbeddings(),
        LocalFileStore("./data/embedding_db"),
        namespace="slgtest")
    embeddings = cached_embedder.embed_documents(["你好", "智能鲜花客服", '马王爷有7只眼', '哈利波特别大'])
    print("共生成向量个数:", len(embeddings))
    print("openai 向量长度", len(embeddings[0]))
    print("openai 向量长度", len(embeddings[1]))
    print("openai 向量长度", len(embeddings[2]))
    print("openai 向量长度", len(embeddings[3]))


def retrieve_default():
    loader = TextLoader("./data/questions.txt", encoding="utf8")
    index = VectorstoreIndexCreator().from_loaders([loader])
    result = index.query("哈利波特是谁？")
    print(result)


def retrieve_from_config():
    loader = TextLoader("./data/questions.txt", encoding="utf8")
    index = VectorstoreIndexCreator(
        vectorstore_cls=Chroma,
        embedding=OpenAIEmbeddings(),
        text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    ).from_loaders([loader])
    result = index.query("马王爷有几只眼？")
    print(result)


def retrieve_from_local_file_by_chroma():
    loader = TextLoader("./data/questions.txt", encoding="utf8")
    index = VectorstoreIndexCreator(
        embedding=OpenAIEmbeddings(),
        text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    ).from_loaders([loader])
    result = index.query("马王爷有几只眼？")
    print(result)


def load_embeddings_from_file(file_path):
    # 假设您的向量数据是以pickle格式保存的
    with open(file_path, 'rb') as f:
        embeddings = pickle.load(f)
    return embeddings


def retrieve_from_local_file(question):
    cached_embedder = CacheBackedEmbeddings.from_bytes_store(
        OpenAIEmbeddings(),
        LocalFileStore("./data/embedding_db"),
        namespace="slgtest")

    # 这玩意不是查询，而是把查询语句弄成向量……
    embedding_answer = cached_embedder.embed_query(question)
    print(embedding_answer)


if __name__ == '__main__':
    print("hello")
    save_to_local_file()
