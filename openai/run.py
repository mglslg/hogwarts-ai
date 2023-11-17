from openai import OpenAI
client = OpenAI()

thread_messages = client.beta.threads.messages.list("thread_9s3MhO8HhGAmGb5tlOtrdNWw")
print(thread_messages.data)
