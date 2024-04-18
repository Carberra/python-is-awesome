import sqlite3
from pathlib import Path
from sqlite3 import Connection
from typing import Iterator

from pydantic import BaseModel

from fastapi import Depends, FastAPI, HTTPException

DB_PATH = Path("db.sqlite3")
SCRIPT_PATH = Path("app/schema.sql")

app = FastAPI(title="Carberra App", version="1.0.0")


class Fact(BaseModel):
    id: int
    body: str


def get_db() -> Iterator[Connection]:
    with sqlite3.connect(DB_PATH, check_same_thread=False) as cxn:
        cxn.executescript(SCRIPT_PATH.read_text())
        cxn.row_factory = sqlite3.Row
        yield cxn


@app.get("/")
def index() -> dict[str, str]:
    return {"message": "Hello world!"}


@app.post("/fact", status_code=201, response_model=Fact)
def create_fact(body: str, db: Connection = Depends(get_db)) -> Fact:
    db.execute("INSERT INTO facts (body) VALUES (?)", (body,))
    return Fact(**db.execute("SELECT * FROM facts ORDER BY id DESC LIMIT 1").fetchone())


@app.get("/fact/{fact_id}", response_model=Fact)
def get_fact(fact_id: int, db: Connection = Depends(get_db)) -> Fact:
    fact = db.execute("SELECT * FROM facts WHERE id = ?", (fact_id,)).fetchone()
    if not fact:
        raise HTTPException(404, "Fact not found")

    return Fact(**fact)


@app.delete("/fact/{fact_id}", status_code=204)
def delete_fact(fact_id: int, db: Connection = Depends(get_db)) -> None:
    rowcount = db.execute("DELETE FROM facts WHERE id = ?", (fact_id,)).rowcount
    if not rowcount:
        raise HTTPException(404, "Fact not found")
