import random


def generate_hex(digits: int) -> str:
    return "%x" % random.randint(0, 16**digits - 1)


if __name__ == "__main__":
    import click

    @click.command()
    @click.option("-d", "--digits", default=7, type=int)
    def cli(digits: int) -> None:
        print(generate_hex(digits))

    cli()
