from openai import OpenAI

client = OpenAI()

who_are_you_thread = client.beta.threads.create()
print(who_are_you_thread)

who_are_you_thread_id = 'thread_9s3MhO8HhGAmGb5tlOtrdNWw'
