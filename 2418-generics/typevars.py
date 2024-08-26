from typing import TypeVar

T = TypeVar("T")


def echo(value: T) -> T:
    return value


x = echo(2)
y = echo("str")
