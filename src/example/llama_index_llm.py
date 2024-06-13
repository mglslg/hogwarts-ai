from llama_index.core import SimpleDirectoryReader, SummaryIndex
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings


class SlgLLM(OpenAI):
    def hello(self):
        return "Hello World!" + self.api_key
    

# define our LLM
Settings.llm = SlgLLM()

# define embed model
Settings.embed_model = "gpt-3.5-turbo"

# Load the your data
documents = SimpleDirectoryReader("./data").load_data()
index = SummaryIndex.from_documents(documents)

# Query and print response
query_engine = index.as_query_engine()
response = query_engine.query("<query_text>")
print(response)
