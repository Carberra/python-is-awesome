from pydantic import validate_arguments


@validate_arguments
def add(x: int, y: int) -> int:
    print(type(x))
    return x + y


print(add("meme", 5))
