from more_itertools import bucket

fruits = {
    "apple": "red",
    "banana": "yellow",
    "cherry": "red",
    "date": "red",
    "grape": "purple",
    "kiwi": "green",
    "lemon": "yellow",
    "lime": "green",
    "mango": "yellow",
    "orange": "orange",
    "pear": "green",
    "pineapple": "yellow",
    "plum": "purple",
    "raspberry": "red",
}

buckets = bucket(fruits, key=lambda fruit: fruits[fruit])
print(list(buckets))
print(list(buckets["yellow"]))
