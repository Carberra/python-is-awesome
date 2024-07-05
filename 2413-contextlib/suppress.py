from contextlib import suppress

if __name__ == "__main__":
    try:
        1 / 0
    except ZeroDivisionError:
        pass

    with suppress(ZeroDivisionError):
        1 / 0
