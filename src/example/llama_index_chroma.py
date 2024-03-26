import chromadb
from llama_index.vector_stores import ChromaVectorStore
from llama_index.storage.storage_context import StorageContext
from llama_index import VectorStoreIndex, SimpleDirectoryReader


def llama_index_chroma():
    # assign chroma as the vector_store to the context
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    documents = SimpleDirectoryReader("./data").load_data()

    index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)

    # create your index
    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context
    )

    # create a query engine and query
    query_engine = index.as_query_engine()
    response = query_engine.query("What is the meaning of life?")
    print(response)

    db = chromadb.PersistentClient(path="./chroma_db")
    chroma_collection = db.get_or_create_collection("quickstart")

    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    index = VectorStoreIndex.from_vector_store(vector_store, storage_context=storage_context)

    query_engine = index.as_query_engine()
    response = query_engine.query("What is llama2?")
    print(response)

    # initialize client
    db = chromadb.PersistentClient(path="./chroma_db")

    # get collection
    chroma_collection = db.get_or_create_collection("quickstart")

    # assign chroma as the vector_store to the context
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # load your index from stored vectors
    index = VectorStoreIndex.from_vector_store(
        vector_store, storage_context=storage_context
    )

    # create a query engine
    query_engine = index.as_query_engine()
    response = query_engine.query("What is llama2?")
    print(response)
