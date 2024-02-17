import time
from multiprocessing import Process
from urllib.request import urlopen


def do_cpu_work() -> int:
    for i in range(20_000):
        2**i


def do_io_work() -> None:
    urlopen("https://youtube.com")


if __name__ == "__main__":
    processes = []
    start = time.perf_counter()

    for _ in range(10):
        p = Process(target=do_cpu_work)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"{time.perf_counter() - start:.2f}s")
