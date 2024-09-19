# from random import sample

from more_itertools import sample

fruits = (
    "apple",
    "banana",
    "cherry",
    "date",
    "grape",
    "kiwi",
    "lemon",
    "lime",
    "mango",
    "orange",
    "pear",
    "pineapple",
    "plum",
    "raspberry",
)

e_fruits = (f for f in fruits if "e" in f)

selection = sample(e_fruits, 3)
print(selection)
