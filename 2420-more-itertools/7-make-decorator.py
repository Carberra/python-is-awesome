from more_itertools import make_decorator, sample

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

sample_three = make_decorator(sample)(3)


@sample_three
def get_all_yellow_fruits(fruits):
    return [fruit for fruit in fruits if fruits[fruit] == "yellow"]


print(list(get_all_yellow_fruits(fruits)))
