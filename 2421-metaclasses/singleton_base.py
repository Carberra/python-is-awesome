import sqlite3
from typing import Any, Self


class Singleton:
    _instance = None

    def __new__(cls, *args: Any, **kwargs: Any) -> Self:
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


class DatabaseManager(Singleton):
    def __init__(self, db_file: str) -> None:
        self._connection = sqlite3.connect(db_file)

    def fetch(self, stmt: str, *args: Any) -> Any:
        return self._connection.execute(stmt, args).fetchone()


if __name__ == "__main__":
    dbm1 = DatabaseManager(":memory:")
    dbm2 = DatabaseManager(":memory:")
    print(dbm1 is dbm2)
