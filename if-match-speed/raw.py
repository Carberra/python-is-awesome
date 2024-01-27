from textwrap import dedent
from timeit import timeit

N = 10_000_000

if_only = dedent(
    """
    if char == "a":
        ...
    if char == "b":
        ...
    if char == "c":
        ...
    if char == "d":
        ...
    ...
    """
)

if_else = dedent(
    """
    if char == "a":
        ...
    elif char == "b":
        ...
    elif char == "c":
        ...
    elif char == "d":
        ...
    else:
        ...
    """
)

match_only = dedent(
    """
    match char:
        case "a":
            ...
        case "b":
            ...
        case "c":
            ...
        case "d":
            ...
        case _:
            ...
    """
)


if __name__ == "__main__":
    char = "e"

    # t = timeit("(i for i in range(1000))")

    t = timeit(match_only, globals={"char": char}, number=N)
    print(f"Match: {t:.3f}s")

    t = timeit(if_only, globals={"char": char}, number=N)
    print(f"If: {t:.3f}s")

    t = timeit(if_else, globals={"char": char}, number=N)
    print(f"If-else: {t:.3f}s")
