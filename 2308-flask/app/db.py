import sqlite3

import click
from flask import current_app, g


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DB_PATH"])
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(exc=None):
    if db := g.pop("db", None):
        db.close()


@click.command("init-db")
def init_db_command():
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf-8"))


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
