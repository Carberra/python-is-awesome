import datetime as dt
from functools import cached_property


class Profile:
    def __init__(self, name: str, birthdate: dt.date) -> None:
        self.name = name
        self.birthdate = birthdate

    @cached_property
    def age(self) -> int:
        print("Calculating age...")
        return (dt.date.today() - self.birthdate).days // 365


if __name__ == "__main__":
    ethan = Profile("Ethan", dt.date(2000, 9, 22))
    print(ethan.age)
    ethan.birthdate = dt.date(1998, 9, 22)
    print(ethan.age)
