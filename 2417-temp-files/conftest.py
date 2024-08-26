import os
from pathlib import Path
from tempfile import NamedTemporaryFile, TemporaryDirectory
from typing import TYPE_CHECKING, Iterator
from unittest import mock

import pytest

if TYPE_CHECKING:
    from tempfile import _TemporaryFileWrapper


@pytest.fixture()
def alembic_ini() -> Iterator["_TemporaryFileWrapper"]:
    with (
        TemporaryDirectory() as d,
        NamedTemporaryFile(suffix=".ini") as ini,
        mock.patch.dict(os.environ, {"ALEMBIC_CONFIG": ini.name}),
    ):
        contents = f"[alembic]\nscript_location = {d}"
        ini.write(contents.encode("utf-8"))
        ini.flush()
        Path(f"{d}/env.py").touch()
        yield ini


def test_invocation(alembic_ini):
    assert alembic_ini
