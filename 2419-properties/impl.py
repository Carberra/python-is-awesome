from typing import Callable, Generic, TypeVar, overload

O = TypeVar("O", bound=object)
T = TypeVar("T")


class Property(Generic[O, T]):
    def __init__(
        self: "Property[O, T]",
        fget: Callable[[O], T] | None = None,
        fset: Callable[[O, T], None] | None = None,
        fdel: Callable[[O], None] | None = None,
        doc: str | None = None,
    ) -> None:
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

        self._name = ""

    def __set_name__(self, owner: O, name: str) -> None:
        self._name = name

    @overload
    def __get__(self, obj: None, objtype: type | None = None) -> "Property[O, T]": ...

    @overload
    def __get__(self, obj: O, objtype: type | None = None) -> T: ...

    def __get__(
        self,
        obj: O | None,
        objtype: type | None = None,
    ) -> "Property[O, T]" | T:
        if obj is None:
            return self

        if self.fget is None:
            raise AttributeError(
                f"property {self._name!r} of {type(obj).__name__!r} object has no getter"
            )

        return self.fget(obj)

    def __set__(self, obj: O, value: T) -> None:
        if self.fset is None:
            raise AttributeError(
                f"property {self._name!r} of {type(obj).__name__!r} object has no setter"
            )

        self.fset(obj, value)

    def __delete__(self, obj: O) -> None:
        if self.fdel is None:
            raise AttributeError(
                f"property {self._name!r} of {type(obj).__name__!r} object has no deleter"
            )

        self.fdel(obj)

    def getter(self: "Property[O, T]", fget: Callable[[O], T]) -> "Property[O, T]":
        self.fget = fget
        return self

    def setter(
        self: "Property[O, T]",
        fset: Callable[[O, T], None],
    ) -> "Property[O, T]":
        self.fset = fset
        return self

    def deleter(self: "Property[O, T]", fdel: Callable[[O], None]) -> "Property[O, T]":
        self.fdel = fdel
        return self
