from more_itertools import collapse

fruits = [
    ["apple", "banana"],
    ["cherry", ["date", "grape"], "kiwi"],
    ["lemon", "lime", ["mango"]],
    "orange",
    "pear",
    [["pineapple", "plum"], "raspberry"],
]

print(list(collapse(fruits)))
