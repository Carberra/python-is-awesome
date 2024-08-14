import os
from functools import cached_property


class Setting:
    def __init__(self, key: str, *, default: str) -> None:
        self.key = key
        self.default = default

    @cached_property
    def value(self) -> str:
        return os.environ.get(self.key, self.default)

    def __get__(self, obj: object, objtype: type | None = None) -> str:
        return self.value


class Config:
    TEST = Setting("TEST", default="test")


if __name__ == "__main__":
    print(Config.TEST)
