import chromadb
from llama_index.core import VectorStoreIndex
from llama_index_client.types import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.core.readers.file.base import SimpleDirectoryReader


def llama_index_chroma():
    # load some documents
    # documents = SimpleDirectoryReader(input_dir="./data", input_files=[".data/questions.txt"]).load_data()
    documents = SimpleDirectoryReader(input_dir="./data").load_data()

    # initialize client, setting path to save data
    db = chromadb.PersistentClient(path="./chroma_db_llama_index")

    # create collection
    chroma_collection = db.get_or_create_collection("quickstart")

    # assign chroma as the vector_store to the context
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # create your index
    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context
    )

    # create a query engine and query
    query_engine = index.as_query_engine()
    response = query_engine.query("伏地魔是谁？")
    print(response)


if __name__ == '__main__':
    llama_index_chroma()
