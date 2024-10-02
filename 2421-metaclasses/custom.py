from typing import Any, Generic, TypeVar

T = TypeVar("T")


class ProfileMeta(Generic[T], type):
    def __init__(
        cls,
        name: str,
        bases: tuple[type, ...],
        attrs: dict[str, Any],
    ) -> None:
        print("Creating class of name:", name)
        print(f"{name=}, {bases=}, {attrs=}")
        super().__init__(name, bases, attrs)

    def __call__(cls, *args: Any, **kwargs: Any) -> T:
        print("Creating instance of class:", cls.__name__)
        print(f"{args=}, {kwargs=}")
        return super().__call__(*args, **kwargs)


class BaseProfile:
    x = 5


class Profile(BaseProfile, metaclass=ProfileMeta):
    def __init__(self, name: str, age: int, job: str) -> None:
        self.name = name
        self.age = age
        self.job = job

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old."


if __name__ == "__main__":
    p = Profile("Ethan", 25, job="Software Engineer")
    print(p)
