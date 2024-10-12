from enum import StrEnum


class Colour(StrEnum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


if __name__ == "__main__":
    print(Colour.RED + Colour.GREEN)
