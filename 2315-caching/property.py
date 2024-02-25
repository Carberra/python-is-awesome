from functools import cached_property


class Number:
    def __init__(self, n, /):
        self.n = n

    @cached_property
    def is_prime(self):
        print(f"Calculating if {self.n} is prime...")

        if self.n == 1:
            return False

        for i in range(2, self.n):
            if self.n % i == 0:
                return False

        return True


if __name__ == "__main__":
    n = Number(69)
    print(n.is_prime)
    print(n.is_prime)
