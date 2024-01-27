from textwrap import dedent
from timeit import timeit

RUNS = 250_000

if __name__ == "__main__":
    update = dedent(
        """
        x = {}
        for i in range(255):
            x.update({chr(i): i})
        """
    )
    assign = dedent(
        """
        x = {}
        for i in range(255):
            x[chr(i)] = i
        """
    )

    ta = timeit(update, number=RUNS)
    tk = timeit(assign, number=RUNS)

    print(f"Dict append: {ta:.3f}s")
    print(f"Dict assign: {tk:.3f}s")
