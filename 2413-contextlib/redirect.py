import sys
from contextlib import redirect_stderr, redirect_stdout

if __name__ == "__main__":
    with open("help.txt", "w") as f:
        with redirect_stdout(f):
            help(pow)

        print("Hello world!")

    with open("error.txt", "w") as f:
        with redirect_stdout(f):
            with redirect_stderr(f):
                print("Hello stdout!")
                print("Hello world!", file=sys.stderr)
