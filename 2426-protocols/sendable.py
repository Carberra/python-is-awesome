from typing import Any, Protocol


class Sendable(Protocol):
    def send(self, message: str, **kwargs: Any) -> None: ...


class Channel:
    def send(self, message: str, *, anonymous: bool = False) -> None: ...


def send_to(sendable: Sendable, message: str) -> None:
    sendable.send(message, anonymous=True)


if __name__ == "__main__":
    send_to(Channel(), "Hello")
