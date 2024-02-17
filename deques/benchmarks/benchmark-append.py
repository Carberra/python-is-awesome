from collections import deque
from random import randint
from timeit import timeit

N = 1_000_000

for i in range(0, (N // 10) + 1, N // 100):
    numbers = [randint(1, 100) for _ in range(N)]
    d_numbers = deque(numbers)

    t0 = timeit(
        "numbers.append(i)", globals={"numbers": numbers, "i": i}, number=N // 10
    )
    t1 = timeit(
        """numbers.append(i)""",
        globals={"numbers": d_numbers, "i": i},
        number=N // 10,
    )

    print(f"For index {i:,}:")
    print(f"   List: {t0:.3f}")
    print(f"  Deque: {t1:.3f}")
    print()
