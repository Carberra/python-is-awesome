import random
from contextlib import contextmanager
from typing import Iterator


@contextmanager
def seed(a: int | float | str | bytes | bytearray | None = None) -> Iterator[None]:
    random.seed(a)
    try:
        print("Yielding")
        yield
    finally:
        print("Resetting seed")
        random.seed()


@seed(42)
def random_numbers(n: int = 3) -> list[int]:
    return [random.randint(1, 10) for _ in range(n)]


if __name__ == "__main__":
    # with seed(42):
    #     print(random.random())
    # 1 / 0
    # print(random.random())

    print(random_numbers())
    print(random.randint(1, 10))
