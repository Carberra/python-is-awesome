from typing import Callable, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class DefaultDict(dict[K, V]):
    def __init__(self, default_factory: Callable[[K], V]) -> None:
        self.default_factory = default_factory

    def __missing__(self, key: K) -> V:
        return self.default_factory(key)
