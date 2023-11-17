from openai import OpenAI
client = OpenAI()

message = client.beta.threads.messages.retrieve(
    message_id="msg_BAqba4QIq3877Fz2OJmkkDTz",
    thread_id="thread_9s3MhO8HhGAmGb5tlOtrdNWw",
)
print(message)
