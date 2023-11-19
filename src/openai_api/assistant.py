from openai import OpenAI

client = OpenAI()


def create_assistant(name, description):
    math_tutor_assistant = client.beta.assistants.create(
        instructions=description,
        name=name,
        tools=[{"type": "code_interpreter"}],
        model="gpt-4-1106-preview",
    )
    print(math_tutor_assistant.model_dump_json)
    return math_tutor_assistant.id


def create_thread():
    new_thread = client.beta.threads.create()
    print("thread created:", new_thread.id)
    return new_thread.id


def get_thread_by_id(thread_id):
    my_thread = client.beta.threads.retrieve(thread_id)
    print("retrieved thread:", my_thread.model_dump_json())
    return my_thread


def list_message(message_id, thread_id):
    message = client.beta.threads.messages.retrieve(
        message_id=message_id,
        thread_id=thread_id,
    )
    print(message)
    return message


def create_message():
    thread_message = client.beta.threads.messages.create(
        "thread_9s3MhO8HhGAmGb5tlOtrdNWw",
        role="user",
        content="Who are you and what do you do?",
    )
    print(thread_message)


def run(assistant_id, thread_id):
    run_obj = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )
    return run_obj.id
