from typing import Annotated

import msgspec
from msgspec import Meta, Struct, field


class Profile(Struct):
    name: str
    age: Annotated[int, Meta(gt=0)]
    jobs: list[str] = field(default_factory=list)

    def encode(self) -> bytes:
        return msgspec.json.encode(self)


if __name__ == "__main__":
    p = Profile("Ethan", -1)
    print(p)

    profile_data = msgspec.json.encode(p)
    print(profile_data)
    p2 = msgspec.json.decode(profile_data, type=Profile)
    print(p2)
