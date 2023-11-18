from openai import OpenAI


def create_thread():
    client = OpenAI()
    new_thread = client.beta.threads.create()
    print("thread created:", new_thread.id)
    return new_thread.id


def get_thread_by_id(thread_id):
    client = OpenAI()
    my_thread = client.beta.threads.retrieve(thread_id)
    print("retrieved thread:", my_thread)
    return my_thread
