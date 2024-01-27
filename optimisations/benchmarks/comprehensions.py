from textwrap import dedent
from timeit import timeit

RUNS = 250_000

if __name__ == "__main__":
    append = dedent(
        """
        x = []
        for i in range(255):
            x.append(chr(i))
        """
    )
    compre = "[chr(i) for i in range(255)]"

    ta = timeit(append, number=RUNS)
    tc = timeit(compre, number=RUNS)

    print(f"List append: {ta:.3f}s")
    print(f"List compr.: {tc:.3f}s")

    append = dedent(
        """
        x = set()
        for i in range(255):
            x.add(chr(i))
        """
    )
    compre = "{chr(i) for i in range(255)}"

    ta = timeit(append, number=RUNS)
    tc = timeit(compre, number=RUNS)

    print(f" Set append: {ta:.3f}s")
    print(f" Set compr.: {tc:.3f}s")

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
    compre = "{chr(i): i for i in range(255)}"

    ta = timeit(update, number=RUNS)
    tk = timeit(assign, number=RUNS)
    tc = timeit(compre, number=RUNS)

    print(f"Dict append: {ta:.3f}s")
    print(f"Dict assign: {tk:.3f}s")
    print(f"Dict compr.: {tc:.3f}s")
