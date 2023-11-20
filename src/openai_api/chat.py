import time

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
    # record the time before the request is sent
    start_time = time.time()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": msg}
        ],
        stream=True
    )

    # create variables to collect the stream of chunks
    collected_chunks = []
    collected_messages = []

    # iterate through the stream of events
    for chunk in response:
        chunk_time = time.time() - start_time  # calculate the time delay of the chunk
        collected_chunks.append(chunk)  # save the event response

        # Check if there are choices and extract the message from the first choice
        if chunk.choices:
            first_choice = chunk.choices[0]  # get the first choice
            delta = first_choice.delta  # get the delta from the choice
            chunk_message = delta.content if delta.content is not None else ''  # get the content from the delta
            collected_messages.append(chunk_message)  # save the message
            print(f"Message received {chunk_time:.2f} seconds after request: {chunk_message}")  # print the delay and text
        else:
            print(f"No choices available for this chunk, received after {chunk_time:.2f} seconds")

    # print the time delay and text received
    print(f"Full response received {chunk_time:.2f} seconds after request")
    full_reply_content = ''.join(collected_messages)  # join all collected messages
    print(f"Full conversation received: {full_reply_content}")


send_msg_stream('chunk是什么意思')

