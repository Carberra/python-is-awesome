import os
from typing import Callable, Generic, TypeVar, cast, overload

T = TypeVar("T")
C = TypeVar("C")


class EnvVar(Generic[T]):
    @overload
    def __init__(self: "EnvVar[str | None]", name: str) -> None: ...

    @overload
    def __init__(self: "EnvVar[str]", name: str, *, default: str) -> None: ...

    @overload
    def __init__(
        self: "EnvVar[C]",
        name: str,
        *,
        default: str | None = None,
        converter: Callable[[str | None], C] | None = None,
    ) -> None: ...

    def __init__(
        self,
        name: str,
        *,
        default: str | None = None,
        converter: Callable[[str | None], C] | None = None,
    ) -> None:
        self.name = name
        self.default = default
        self.converter = converter

    @property
    def value(self) -> T:
        value = os.environ.get(self.name, self.default)

        if self.converter:
            return cast(T, self.converter(value))

        return cast(T, value)


def as_int(value: str | None) -> int:
    return int(value) if value else 0


if __name__ == "__main__":
    EnvVar("FOO").value
    EnvVar("FOO", default="bar").value
    EnvVar("FOO", converter=bool).value
