import asyncio

import openai
from openai import ChatCompletion

with open("key.txt") as f:
    openai.api_key = f.read().strip()

history = []


async def send(content):
    history.append({"role": "user", "content": content})
    resp = await ChatCompletion.acreate(model="gpt-3.5-turbo", messages=history)
    output = resp["choices"][0]["message"]["content"]
    history.append({"role": "assistant", "content": output})
    return output


async def main():
    while True:
        user_input = input("> ")
        assistant_output = await send(user_input)
        print(assistant_output, end="\n\n")


asyncio.run(main())
