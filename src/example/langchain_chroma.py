import chromadb
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma


def retrieve_default():
    loader = TextLoader("./data/questions.txt", encoding="utf8")
    index = VectorstoreIndexCreator().from_loaders([loader])
    result = index.query("哈利波特是谁？")
    print(result)


def retrieve_from_local_file_by_chroma():
    loader = TextLoader("./data/questions.txt", encoding="utf8")
    index = VectorstoreIndexCreator(
        embedding=OpenAIEmbeddings(),
        text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    ).from_loaders([loader])
    result = index.query("马王爷有几只眼？")
    print(result)


def retrieve_from_chroma():
    loader = TextLoader("./data/questions.txt", encoding="utf8")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    docs = text_splitter.split_documents(documents)
    vectordb = Chroma.from_documents(documents=docs, embedding=OpenAIEmbeddings(), persist_directory="./data/chroma_db")

    vectordb.add_texts("张三打死了二狗")
    vectordb.add_texts("李四爱抽烟")

    vectordb.persist()

    # embeddings = util.get_embeddings("抽烟")
    # docs1 = vectordb.similarity_search_by_vector(embeddings)
    docs1 = vectordb.similarity_search("张三")

    print(docs1[0].page_content)


def original_chroma():
    client = chromadb.PersistentClient(path="./data/chroma_db")
    print(client.heartbeat())
    # persistant_client.reset()

    collection = client.get_collection(name="my_collection")
    if not collection:
        collection = client.create_collection(name="my_collection")

    collection.add()


if __name__ == '__main__':
    # retrieve_from_local_file_by_chroma()
    # original_chroma()
    retrieve_from_chroma()
