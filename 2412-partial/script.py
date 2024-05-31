from functools import partialmethod


class Test:
    def mult(self, x: int, y: int) -> int:
        return x * y

    double = partialmethod(mult, 2)


if __name__ == "__main__":
    print(Test().double(5))
