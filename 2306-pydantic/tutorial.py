from pydantic import BaseModel, validator


def to_camel_case(text):
    camel_string = "".join(x.capitalize() for x in text.lower().split("_"))
    return text[0].lower() + camel_string[1:]


class Profile(BaseModel):
    name: str
    age: int
    my_jobs: list[str] = []

    class Config:
        validate_assignment = True
        alias_generator = to_camel_case

    @validator("age")
    def age_gt_0(cls, value: int) -> int:
        if value < 0:
            raise ValueError("age must be greater than zero")
        return value


resp = {"name": "Ethan", "age": 24, "my_jobs": ("meme",)}
# p = Profile(name="Ethan", age=24, jobs=["Software Engineer"])
p = Profile(**resp)
print(p)
p.age = -1
print(p.age)
