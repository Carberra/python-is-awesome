def str_to_bool(value: str) -> bool:
    """Convert a string to a boolean.

    Examples
    --------
    >>> str_to_bool("true")
    True
    >>> str_to_bool("false")
    False
    >>> str_to_bool("hello world")
    Traceback (most recent call last):
        ...
    ValueError: invalid boolean value: 'hello world'
    """
    if (value := value.lower()) in ("false", "f", "0"):
        return False
    if (value := value.lower()) in ("true", "t", "1"):
        return True
    raise ValueError(f"invalid boolean value: {value!r}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
