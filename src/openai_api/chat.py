from openai import OpenAI

client = OpenAI()


def send_msg(msg):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": msg}
        ]
    )
    return completion.choices[0].message
