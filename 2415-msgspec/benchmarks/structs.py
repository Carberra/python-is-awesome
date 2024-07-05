from timeit import repeat

from tabulate import tabulate

N = 1_000_000

pydantic_setup = """
from pydantic import BaseModel, Field, field_validator

class Profile(BaseModel):
    name: str
    age: int
    jobs: list[str] = Field(default_factory=list)

    @field_validator("age")
    def age_gt_0(cls, v):
        if v <= 0:
            raise ValueError("Age must be greater than 0")
        return v
"""


msgspec_setup = """
from typing import Annotated

import msgspec
from msgspec import Meta, Struct, field

class Profile(Struct, kw_only=True):
    name: str
    age: Annotated[int, Meta(gt=0)]
    jobs: list[str] = field(default_factory=list)
"""

data = '{"name": "Ethan", "age": 25, "jobs": ["Software Engineer"]}'

t0 = min(
    repeat(
        "Profile.model_validate_json(data)",
        setup=pydantic_setup,
        globals={"data": data},
    )
)
t1 = min(
    repeat(
        "msgspec.json.decode(data, type=Profile)",
        setup=msgspec_setup,
        globals={"data": data},
    )
)

t2 = min(
    repeat(
        "p.model_dump_json()",
        setup=(
            pydantic_setup
            + "p = Profile(name='Ethan', age=25, jobs=['Software Engineer'])"
        ),
    )
)
t3 = min(
    repeat(
        "msgspec.json.encode(p)",
        setup=(
            msgspec_setup
            + "p = Profile(name='Ethan', age=25, jobs=['Software Engineer'])"
        ),
    )
)

table = [
    ("Decoding", t0 / N * 1e9, t1 / N * 1e9, t0 / t1),
    ("Encoding", t2 / N * 1e9, t3 / N * 1e9, t2 / t3),
]

print(
    tabulate(
        table,
        headers=["Test", "Pydantic (ns)", "Msgspec (ns)", "Speedup (x)"],
        floatfmt=",.1f",
    )
)
