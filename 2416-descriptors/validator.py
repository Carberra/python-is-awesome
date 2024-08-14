class AgeValidator:
    def __set_name__(self, owner: type, name: str) -> None:
        self.private_name = f"_{name}"

    def __get__(self, obj: "Person", objtype: type | None = None) -> int:
        return getattr(obj, self.private_name)

    def __set__(self, obj: "Person", value: int) -> None:
        if value < 0:
            raise ValueError(f"{self.private_name!r} must be positive")

        setattr(obj, self.private_name, value)


class Person:
    _age: int
    years = AgeValidator()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.years = age


if __name__ == "__main__":
    person = Person("John", 10)
    print(person.years)
    person.years = -10
