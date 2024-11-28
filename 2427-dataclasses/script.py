from dataclasses import KW_ONLY, dataclass, field
from enum import Enum, auto


class Gender(Enum):
    MALE = auto()
    FEMALE = auto()
    USER_SPECIFIED = auto()


@dataclass(frozen=True)
class Profile:
    name: str
    age: int
    _: KW_ONLY
    gender: Gender = Gender.USER_SPECIFIED
    jobs: list[str] = field(default_factory=list)


if __name__ == "__main__":
    profile1 = Profile("Ethan", 26, gender=Gender.MALE, jobs=["Engineer", "Developer"])
    print(hash(profile1))
    profile2 = Profile("Ethan", 25)
