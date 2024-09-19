from more_itertools import unique

fruits = (
    "apple",
    "banana",
    "cherry",
    "cherry",
    "grape",
    "kiwi",
    "lemon",
    "lemon",
    "lemon",
    "orange",
    "pear",
    "pineapple",
    "pineapple",
    "raspberry",
)

for fruit in unique(fruits):
    print(fruit.upper())
