import openai
from openai import ChatCompletion

with open("key.txt") as f:
    openai.api_key = f.read().strip()

response = ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "How far is Earth away from the sun?"}],
)
print(response)
