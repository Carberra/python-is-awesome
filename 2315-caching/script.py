from functools import cache, lru_cache


@cache
def add(x, y):
    print(f"Adding {x} and {y} together!")
    return x + y


@lru_cache(maxsize=3)
def square(x):
    print(f"Squaring {x}!")
    return x**2


if __name__ == "__main__":
    print(square(1))
    print(square(2))
    print(square(3))
    print(square(1))
    print(square(4))
    print(square(2))
