from more_itertools import triplewise, windowed

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

for triple in triplewise(fruits):
    print(triple)

for window in windowed(fruits, 6, step=3):
    print(window)
