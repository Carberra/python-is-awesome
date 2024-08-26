from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass()
class Apple:
    name: str = "apple"


@dataclass()
class Banana:
    name: str = "banana"


class Box(Generic[T]):
    def __init__(self) -> None:
        self.items: list[T] = []

    def add(self, item: T) -> None:
        self.items.append(item)

    def remove(self, item: T) -> None:
        self.items.remove(item)


if __name__ == "__main__":
    apple_box = Box[Banana]()
    apple_box.add(Apple())
    apple_box.add(Banana())
