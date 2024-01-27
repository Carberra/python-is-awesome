from timeit import timeit

N = 10_000_000


def if_only(char):
    if char == "a":
        return 1
    if char == "b":
        return 2
    if char == "c":
        return 3
    if char == "d":
        return 4
    return 0


def if_else(char):
    if char == "a":
        return 1
    elif char == "b":
        return 2
    elif char == "c":
        return 3
    elif char == "d":
        return 4
    else:
        return 0

    return n


def match_only(char):
    match char:
        case "a":
            return 1
        case "b":
            return 2
        case "c":
            return 3
        case "d":
            return 4
        case _:
            return 0


if __name__ == "__main__":
    char = "e"

    t = timeit("func(char)", globals={"char": char, "func": if_only}, number=N)
    print(f"If: {t:.3f}s")

    t = timeit("func(char)", globals={"char": char, "func": if_else}, number=N)
    print(f"If-else: {t:.3f}s")

    t = timeit("func(char)", globals={"char": char, "func": match_only}, number=N)
    print(f"Match: {t:.3f}s")
