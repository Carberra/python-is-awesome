import time
from functools import partial, wraps


def timer(func=None, *, verbose=False):
    if func is None:
        return partial(timer, verbose=verbose)

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        if verbose:
            print(f"{func.__name__} started at {start}")
        result = func(*args, **kwargs)
        end = time.perf_counter_ns()
        if verbose:
            print(f"{func.__name__} ended at {start}")
        print(f"{func.__name__} took {end - start:,.0f}ns")
        return result

    return wrapper


@timer
def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    factorial(1000)
