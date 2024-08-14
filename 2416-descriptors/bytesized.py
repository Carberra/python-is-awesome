class AgeValidator:
    def __get__(self, obj, objtype=None):
        return obj._age

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("age must be positive")

        obj._age = value


class Person:
    age = AgeValidator()

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


john = Person("John", 3)
print(john.age)
amy = Person("Amy", 16)
amy.age = -10
