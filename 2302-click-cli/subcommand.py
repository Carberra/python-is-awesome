import click


@click.group(invoke_without_command=True)
@click.pass_context
def cmd(ctx):
    if ctx.invoked_subcommand:
        return

    print("This is a group command!")


@cmd.command()
def subcmd():
    print("This is a subcommand!")


if __name__ == "__main__":
    cmd()
