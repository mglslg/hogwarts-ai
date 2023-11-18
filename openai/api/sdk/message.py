from openai import OpenAI
client = OpenAI()

thread_message = client.beta.threads.messages.create(
    "thread_9s3MhO8HhGAmGb5tlOtrdNWw",
    role="user",
    content="Who are you and what do you do?",
)
print(thread_message)
