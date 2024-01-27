from timeit import timeit

import matplotlib.pyplot as plt
import seaborn as sns

N = 100
RUNS = 500_000

if __name__ == "__main__":
    sns.set_style("darkgrid")

    fig = plt.figure(figsize=(10, 6))
    plt.xlabel("Number to find")
    plt.ylabel(f"Time to find {RUNS:,} times (s)")

    for i, c in enumerate((list, tuple, set, frozenset)):
        numbers = c(i for i in range(N))
        times = []

        for n in range(N):
            times.append(
                timeit(
                    f"{n} in numbers",
                    globals={"numbers": numbers},
                    number=RUNS,
                )
            )

        sns.lineplot(x=list(numbers), y=times, label=c.__name__.title())

    plt.tight_layout()
    fig.savefig("containment-benchmarks.png")
