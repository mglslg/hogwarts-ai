from api.sdk import run
from api_config import config
from openai import OpenAI


def call_api():
    run.do_run(config.get_assistant_by_name("Math Tutor"), "thread_9s3MhO8HhGAmGb5tlOtrdNWw")


def get_message():
    client = OpenAI()

    thread_messages = client.beta.threads.messages.list("thread_9s3MhO8HhGAmGb5tlOtrdNWw")

    for msg in thread_messages:
        print(msg.model_dump_json())


get_message()
