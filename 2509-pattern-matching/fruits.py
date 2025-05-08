fruit = "banana"
colour = "green"

# if fruit == "apple":
#     if colour in ("red", "green"):
#         print("You have an apple!")
# elif fruit == "banana":
#     if colour == "yellow":
#         print("You have a banana!")
#     elif colour == "purple":
#         print("You have a purple banana! How odd!")
# else:
#     print("Are you sure about that?")


match (fruit, colour):
    case ("apple", "red") | ("apple", "green"):
        print("You have an apple!")
    case ("banana", "yellow"):
        print("You have a banana!")
    case ("banana", "purple"):
        print("You have a purple banana! How odd!")
    case ("banana", _):
        print("You have a weird banana!")
    case _:
        print("Are you sure about that?")
