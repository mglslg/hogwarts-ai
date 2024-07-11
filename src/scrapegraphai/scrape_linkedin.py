import os
from dotenv import load_dotenv
from scrapegraphai.graphs import SmartScraperGraph

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

graph_config = {
    "llm": {
        "api_key": openai_key,
        "model": "gpt-3.5-turbo",
    },
    "verbose": True,
    "max_results": 100,
    # "headless": False
}

# ************************************************
# Create the SmartScraperGraph instance and run it
# ************************************************

smart_scraper_graph = SmartScraperGraph(
    prompt="头条新闻以及它们对应的url地址，输出成json格式,双引号的json",
    # also accepts a string with the already downloaded HTML code
    source="https://edition.cnn.com/world/china",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)
