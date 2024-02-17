import time
from threading import Lock, Thread
from urllib.request import urlopen

lock = Lock()


def do_cpu_work():
    for i in range(20_000):
        2**i


def do_io_work():
    with lock:
        print("start")
        urlopen("https://youtube.com")
        print("end")


if __name__ == "__main__":
    threads = []
    start = time.perf_counter()

    for _ in range(10):
        t = Thread(target=do_io_work)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"{time.perf_counter() - start:.2f}s")
