numbers = [i for i in range(10)]

if any(i % 2 == 0 for i in numbers):
    ...


def custom_any(seq):
    for i in seq:
        if i % 2 == 0:
            return True

    return False
