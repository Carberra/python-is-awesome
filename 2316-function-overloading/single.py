from functools import singledispatchmethod
from numbers import Number


class Test:
    @singledispatchmethod
    def describe(self, arg):
        return "Unknown type."

    @describe.register
    def _(self, arg: str):
        return "A string."

    @describe.register(list)
    @describe.register(tuple)
    @describe.register(set)
    def _(self, arg):
        return f"A collection of {len(arg)} elements."

    @describe.register
    def _(self, arg: Number):
        return "A number."


if __name__ == "__main__":
    t = Test()
    print(t.describe("Hello world!"))
    print(t.describe([1, 2, 3]))
    print(t.describe(5.4))
    print(t.describe({1: "one", 2: "two"}))
