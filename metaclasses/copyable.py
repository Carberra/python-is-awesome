class Copyable(type):
    def __new__(cls, name, bases, dct):
        print("copyable new")
        obj = super().__new__(cls, name, bases, dct)

        def copy(self):
            return self.__class__(**self.__dict__)

        obj.copy = copy
        return obj


class Qux(metaclass=Copyable):
    def __init__(self, name, age, jobs=None):
        print("qux init")
        self.name = name
        self.age = age
        self.jobs = jobs or []


x = Qux("Ethan", 24, ["Software Engineer"])
x = Qux("Ethan", 24, ["Software Engineer"])
# y = x.copy()
# print(x.name, y.name)
# print(x.age, y.age)
# y.age += 1
# print(x.age, y.age)
# print(x.jobs, y.jobs)
