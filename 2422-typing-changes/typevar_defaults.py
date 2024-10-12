from typing import Generic, TypeVar


class Context: ...


T = TypeVar("T", default=Context)


class CustomContext: ...


class App(Generic[T]):
    context: T


if __name__ == "__main__":
    app = App()
    reveal_type(app.context)
