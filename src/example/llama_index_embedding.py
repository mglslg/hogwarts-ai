from typing import Any, List
from llama_index.embeddings.openai import OpenAIEmbedding


class SlgEmbedding(OpenAIEmbedding):
    def hello(self):
        print(super().api_key, "hello")
        print(self.api_key, "hello")
