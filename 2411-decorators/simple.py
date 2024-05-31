import time
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def timer(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.perf_counter_ns()
        result = func(*args, **kwargs)
        delta = time.perf_counter_ns() - start
        print(f"{func.__name__} took {delta:,.0f}ns")
        return result

    return wrapper


@timer
def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print(factorial(100))
    print(factorial.__name__)
