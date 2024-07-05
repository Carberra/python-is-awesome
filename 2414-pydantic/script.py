import datetime as dt

from pydantic import BaseModel, field_validator


class Order(BaseModel):
    id: int
    item_name: str
    quantity: int
    created_at: dt.datetime
    delivered_at: dt.datetime | None = None

    class Config:
        validate_assignment = True

    @field_validator("quantity")
    @classmethod
    def validate_quantity(cls, value: int) -> int:
        print(type(cls))
        if value < 1:
            raise ValueError("`quantity` must be greater than 0")
        return value

    @field_validator("created_at")
    def validate_created_at(cls, value: dt.datetime) -> dt.datetime:
        if value > dt.datetime.now():
            raise ValueError("`created_at` must be in the past")
        return value


if __name__ == "__main__":
    o = Order(
        id=1,
        item_name="test",
        quantity=3,
        created_at=dt.datetime.now(),
        delivered_at=dt.datetime.now() + dt.timedelta(days=1),
    )
    o.quantity = -1
    print(o.quantity)
