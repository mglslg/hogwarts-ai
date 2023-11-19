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

def send_msg_stream(msg):
    responses = []
    with OpenAI.ChatCompletion.stream(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": msg}
        ]
    ) as stream:
        for response in stream:
            responses.append(response)
            # You can process each part of the response as it arrives
            # For example, print it, store it, etc.
            print(response)
    return responses