from typing import Iterable


class Test:
    __class_attr = "class attribute"

    def __init__(self, x: str) -> None:
        self._instance_attr = f"instance {x}"


class Test2(Test):
    __class_attr = "new class attribute"


if __name__ == "__main__":
    # print(Test.__class_attr)
    t = Test("hello")
    # print(t.__instance_attr)
    # print(t.method())
    # print(dir(t))
    # print(Test._Test__class_attr)
    # print(t._Test__instance_attr)
    # print(t._Test__method)

    print(Test2._Test__class_attr)
    print(Test2._Test2__class_attr)
