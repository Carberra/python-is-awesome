import sqlite3
from typing import Any, Generic, TypeVar

T = TypeVar("T")


class SingletonMeta(Generic[T], type):
    _instance: T | None = None

    def __call__(cls, *args: Any, **kwargs: Any) -> T:
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class DatabaseManager(metaclass=SingletonMeta):
    def __init__(self, db_file: str) -> None:
        self._connection = sqlite3.connect(db_file)

    def fetch(self, stmt: str, *args: Any) -> Any:
        return self._connection.execute(stmt, args).fetchone()


if __name__ == "__main__":
    dbm1 = DatabaseManager(":memory:")
    dbm2 = DatabaseManager(":memory:")
    print(dbm1 is dbm2)
