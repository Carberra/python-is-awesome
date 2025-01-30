import dotenv
import mesop as me
import mesop.labs as mel
from openai import OpenAI

dotenv.load_dotenv()

client = OpenAI()


def on_load(event: me.LoadEvent):
    me.set_theme_mode("dark")


@me.page(path="/", title="Carberra chatbot", on_load=on_load)
def page():
    mel.chat(transform, title="CarberraGPT", bot_user="CarberraGPT")


def transform(input: str, history: list[mel.ChatMessage]):
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": msg.role, "content": msg.content} for msg in history],
    )
    yield resp.choices[0].message.content
