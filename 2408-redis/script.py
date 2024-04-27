import pickle
import time
from dataclasses import dataclass

from redis import Redis


@dataclass()
class Profile:
    name: str
    age: int
    jobs: list[str]


if __name__ == "__main__":
    cache = Redis()

    cache.set("Hello", "world")
    print(cache.get("Hello"))

    cache.expire("Hello", 10)
    time.sleep(11)
    print(cache.get("Hello"))
    cache.persist("Hello")

    profile = Profile("Ethan", 25, ["Engineer", "Programmer"])
    print(pickle.dumps(profile))
    cache.set("ethan", pickle.dumps(profile))

    if value := cache.get("ethan"):
        print(pickle.loads(value))  # type: ignore[arg-type]
