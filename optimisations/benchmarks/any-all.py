from timeit import timeit

N = 100
RUNS = 1_000_000


def custom_any_true(numbers):
    for n in numbers:
        if n % 3 == 0 and n % 5 == 0:
            return True

    return False


def custom_any_untrue(numbers):
    for n in numbers:
        if n > N:
            return True

    return False


def custom_all_true(numbers):
    for n in numbers:
        if n > N:
            return False

    return True


def custom_all_untrue(numbers):
    for n in numbers:
        if n < N + 1:
            return False

    return True


if __name__ == "__main__":
    numbers = [i for i in range(N)]

    t0 = timeit(
        "any(l)",
        globals={"numbers": numbers, "l": [n % 3 == 0 and n % 5 == 0 for n in numbers]},
        number=RUNS,
    )
    t1 = timeit(
        "custom_any(numbers)",
        globals={"numbers": numbers, "custom_any": custom_any_true},
        number=RUNS,
    )
    print(f"Builtin any (true) : {t0:.3f}s\n Custom any (true) : {t1:.3f}s")

    t0 = timeit(
        "any(l)",
        globals={
            "numbers": numbers,
            "l": [n % 3 == 999 and n % 5 == 999 for n in numbers],
        },
        number=RUNS,
    )
    t1 = timeit(
        "custom_any(numbers)",
        globals={"numbers": numbers, "custom_any": custom_any_untrue},
        number=RUNS,
    )
    print(f"Builtin any (false): {t0:.3f}s\n Custom any (false): {t1:.3f}s")

    # ALL

    t0 = timeit(
        "all(l)",
        globals={"numbers": numbers, "l": [n < 101 for n in numbers]},
        number=RUNS,
    )
    t1 = timeit(
        "custom_all(numbers)",
        globals={"numbers": numbers, "custom_all": custom_all_true},
        number=RUNS,
    )
    print(f"Builtin all (true) : {t0:.3f}s\n Custom all (true) : {t1:.3f}s")

    t0 = timeit(
        "all(l)",
        globals={"numbers": numbers, "l": [n > 100 for n in numbers]},
        number=RUNS,
    )
    t1 = timeit(
        "custom_all(numbers)",
        globals={"numbers": numbers, "custom_all": custom_all_untrue},
        number=RUNS,
    )
    print(f"Builtin all (false): {t0:.3f}s\n Custom all (false): {t1:.3f}s")
