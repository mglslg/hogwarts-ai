import numpy as np
from langchain_openai import OpenAIEmbeddings


def get_embeddings(text: str):
    if not text:
        return []
    embeddings_model = OpenAIEmbeddings()
    embeddings = embeddings_model.embed_documents([text])
    return embeddings[0]


# cosine计算向量相似度
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# cosine计算向量相似度
def search_docs(df, user_query, top_n=4):
    embedding = get_embeddings(
        user_query
        # model should be set to the deployment name you chose when you deployed the text-embedding-ada-002 (Version 2) model
    )
    df["similarities"] = df.ada_v2.apply(lambda x: cosine_similarity(x, embedding))

    res = (
        df.sort_values("similarities", ascending=False).head(top_n)
    )
    return res
