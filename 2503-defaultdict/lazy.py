import sqlite3
from dataclasses import dataclass

cxn = sqlite3.connect("db.sqlite3")


@dataclass()
class Profile:
    name: str
    age: int
    job: str | None = None


class ProfileDefaultDict(dict[str, Profile]):
    def __missing__(self, key: str) -> Profile:
        row = cxn.execute(
            "SELECT name, age, job FROM profiles WHERE name = ?",
            (key,),
        ).fetchone()

        if row is None:
            raise KeyError(f"record {key!r} does not exist")

        self[key] = Profile(name=row[0], age=row[1], job=row[2])
        return self[key]


profiles = ProfileDefaultDict()

if __name__ == "__main__":
    print(profiles)
    print(profiles["Ethan"])
    print(profiles)
    print(profiles["Bob"])
