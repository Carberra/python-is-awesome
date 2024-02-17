from numbers import Number

from multipledispatch import dispatch


@dispatch()
def add(x: object, y: object) -> str:
    return f"{x} + {y}"


@dispatch()
def add(x: Number, y: Number) -> Number:
    return x + y


@dispatch()
def add(x: Number) -> Number:
    return x + 1


if __name__ == "__main__":
    print(add(1, 2))
    print(add(1.6))
    print(add("1", True))
    print(add("5"))
