from typing import Any, NotRequired, TypedDict


class ProfileT(TypedDict):
    name: str
    age: int
    jobs: NotRequired[list[str]]


NewProfileT = TypedDict(
    "NewProfileT",
    {
        "name": str,
        "age": int,
        "jobs": NotRequired[list[str]],
    },
)


profile: NewProfileT = {
    "name": "Ethan",
    "age": 24,
    "jobs": ["Software Engineer"],
}

profile["gender"] = "Male"
