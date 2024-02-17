Foo = type("Foo", (), {})


class Foo:
    def __call__(self, *args, **kwargs):
        ...


def bar():
    ...
