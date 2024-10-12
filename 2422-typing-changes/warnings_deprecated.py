from warnings import deprecated


@deprecated("Use `hello('world')` instead.")
def hello_world():
    print("Hello world!")


def hello(entity: str = "world"):
    print(f"Hello {entity}!")


hello_world()
hello("world")
