from typing import ReadOnly, TypedDict


class User(TypedDict):
    id: ReadOnly[int]
    name: str
    email: str


user: User = {
    "id": 1,
    "name": "John",
    "email": "j@j.com",
}

user["id"] = 2
