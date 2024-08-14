import abc
from typing import Generic, TypeVar, cast

T = TypeVar("T")


class Validator(Generic[T], metaclass=abc.ABCMeta):
    def __set_name__(self, owner: type, name: str) -> None:
        self.name = name
        self.private_name = "_" + name

    def __get__(self, obj: object, objtype: type | None = None) -> T:
        return cast(T, getattr(obj, self.private_name))

    @abc.abstractmethod
    def __set__(self, obj: object, value: T) -> None:
        pass


class AgeValidator(Validator[int]):
    def __set__(self, obj: object, value: int) -> None:
        if value < 0:
            raise ValueError(f"{self.name!r} must be positive")

        setattr(obj, self.private_name, value)


class Person:
    age = AgeValidator()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


if __name__ == "__main__":
    p = Person("John", 3)
    print(p.age)
    q = Person("Amy", 16)
    q.age = -10
