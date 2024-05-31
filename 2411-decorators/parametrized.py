import time
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

UNITS = ("ns", "us", "ms", "s")

P = ParamSpec("P")
R = TypeVar("R")


def timer(
    unit: str = "ns", *, precision: int = 0
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            start = time.perf_counter_ns()
            result = func(*args, **kwargs)
            delta = (time.perf_counter_ns() - start) / (1000 ** UNITS.index(unit))
            print(f"{func.__name__} took {delta:,.{precision}f}{unit}")
            return result

        return wrapper

    return decorator


@timer("ms", precision=3)
def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print(factorial(100))
    print(factorial.__name__)
