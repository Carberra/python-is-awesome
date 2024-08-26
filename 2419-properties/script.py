class Profile:
    def __init__(self, name: str, age: int, job: str) -> None:
        self.name = name
        self.job = job

        self._age = age

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if value < 0:
            raise ValueError("age cannot be negative")

        self._age = value

    @age.deleter
    def age(self) -> None:
        self._age = 0


if __name__ == "__main__":
    ethan = Profile("Ethan", 25, "Software Engineer")
    print(ethan.age)

    ethan.age = 30
    print(ethan.age)

    del ethan.age
    print(ethan.age)

    print(Profile.age)
