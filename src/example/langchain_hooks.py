from langchain_openai import OpenAIEmbeddings


class MyEmbeddings(OpenAIEmbeddings):
    model = "abc"

    def validate_environment(cls, values: Dict) -> Dict:
        return Dict
