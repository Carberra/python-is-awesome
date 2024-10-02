class BaseProfile:
    x = 5


if __name__ == "__main__":
    print(type(5))
    print(type("Hello"))

    Profile = type(
        "Profile",
        (BaseProfile,),
        {
            "name": "Ethan",
            "age": 25,
            "job": "Software Engineer",
            "__str__": lambda self: f"{self.name} is {self.age} years old.",
        },
    )

    p = Profile()
    print(p)
    print(type(p))
    print(p.name, p.age, p.job)
    print(p.x)
