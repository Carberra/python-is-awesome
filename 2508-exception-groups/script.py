def func() -> None:
    e1 = TypeError("invalid type")
    e2 = ValueError("invalid value")
    e3 = NameError("invalid name")
    e4 = NameError("invalid name 2")

    eg1 = ExceptionGroup("some errors occured", [e1, e2])
    eg2 = ExceptionGroup("some nested errors occured", [eg1, e3, e4])
    raise eg2


if __name__ == "__main__":
    try:
        func()
    except* NameError as e1:
        print(f"{e1 = !r}")
    except* (TypeError, ValueError) as e2:
        print(f"{e2 = !r}")
