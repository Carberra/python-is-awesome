import json
import time
import tracemalloc
from multiprocessing import Process
from threading import Thread
from typing import Callable, Type
from urllib.request import urlopen


def do_cpu_work() -> None:
    """Simulates CPU-intensive work."""
    x = [0]

    for i in range(1_000_000):
        j = x.pop()
        k = i + j - 100
        x.append(k)


def do_io_work() -> None:
    """Simulates network request work."""
    base_url = "https://raw.githubusercontent.com/Carberra/files/master/resources"
    endpoints = [
        "/flask/static/styles.css",
        "/flask/templates/base.html",
        "/flask/templates/auth/login.html",
        "/flask/templates/auth/register.html",
        "/pyscript/jan23.csv",
    ]
    for endpoint in endpoints:
        urlopen(base_url + endpoint)


def run_worker(worker: Type[Thread | Process], callable: Callable[..., None]) -> None:
    """Creates 10 workers and runs the `do_work` function in each."""
    tracemalloc.start()
    start = time.perf_counter()
    workers: list[Thread | Process] = []

    for _ in range(10):
        w = worker(target=callable)
        workers.append(w)
        w.start()

    for w in workers:
        w.join()

    end = time.perf_counter()
    duration = end - start
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Method:            {worker.__name__}")
    print(f"Callable:          {callable.__name__}")
    print(f"Completion time:   {duration:.2f} seconds")
    print(f"Current mem usage: {current_mem:,} bytes")
    print(f"Peak mem usage:    {peak_mem:,} bytes")
    print()


if __name__ == "__main__":
    # run_worker(Thread, do_cpu_work)
    # run_worker(Process, do_cpu_work)
    run_worker(Process, do_io_work)
    # run_worker(Thread, do_io_work)
