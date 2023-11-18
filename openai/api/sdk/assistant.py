from openai import OpenAI
client = OpenAI()

math_tutor_assistant = client.beta.assistants.create(
    instructions="You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
    name="Math Tutor",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview",
)
print(math_tutor_assistant)

# Math Tutor Assistant
math_tutor_assistant_id = 'asst_HhXfMHbakJFuPB7SSSsaWEvG'
