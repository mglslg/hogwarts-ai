import chromadb
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter


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


def use_chroma():
    chroma_client = chromadb.Client()


if __name__ == '__main__':
    retrieve_from_local_file_by_chroma()
