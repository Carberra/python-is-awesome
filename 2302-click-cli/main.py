import click

VERSION = "0.1.0"


@click.command()
@click.version_option(VERSION, message="%(version)s")
@click.argument("names", nargs=2)
@click.option("-a", "--age", type=int, default=0)
# @click.option("-s", "--shout", is_flag=True)
@click.option("--shout/--no-shout")
@click.option("-f", "--file", type=click.File("w"))
def profile(names, age, shout, file):
    text = f"My name is {' '.join(names)} and I am {age} years old!"

    if shout:
        text = text.upper()

    if file:
        print(f"Saving to {file.name}")
        file.write(text)

    print(text)


if __name__ == "__main__":
    profile()
