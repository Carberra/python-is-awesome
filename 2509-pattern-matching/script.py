colour = "red"

if colour == "red":
    print("The colour is red.")
elif colour == "blue":
    print("The colour is blue.")
else:
    print("The colour is not red or blue.")

match colour:
    case "red":
        print("The colour is red.")
    case "blue":
        print("The colour is blue.")
    case _:
        print("The colour is not red or blue.")
