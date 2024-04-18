import random

if __name__ == "__main__":
    while True:
        number = random.randint(1, 10)
        tries = 3

        while tries > 0:
            try:
                guess = int(input("Guess a number between 1 and 10: "))
            except ValueError:
                print("Invalid guess! Try again.")
                continue

            if guess > number:
                print("Too high!")
                tries -= 1
                continue

            if guess < number:
                print("Too low!")
                tries -= 1
                continue

            print("Congrats, you won!")
            break

        else:
            print(f"No more guesses! The number was {number}.")

        if input("Try again? ").casefold() not in ("yes", "y"):
            break
