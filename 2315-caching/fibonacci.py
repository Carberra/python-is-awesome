from functools import cache
from timeit import timeit


@cache
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print("{:.6f}".format(timeit("f(40)", globals={"f": fibonacci}, number=1)))
