import doctest
import unittest
from typing import TYPE_CHECKING

from carberra import math, utils

if TYPE_CHECKING:
    from unittest import TestLoader, TestSuite


def load_tests(
    loader: "TestLoader",
    tests: "TestSuite",
    pattern: str | None,
) -> "TestSuite":
    tests.addTests(
        [
            doctest.DocTestSuite(math),
            doctest.DocTestSuite(utils),
        ]
    )
    return tests


if __name__ == "__main__":
    unittest.main()
