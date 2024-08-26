from pathlib import Path
from tempfile import NamedTemporaryFile, TemporaryDirectory

with NamedTemporaryFile(prefix="t", suffix=".txt") as f:
    print(f.name)
    temppath = Path(f.name)
    print(temppath.is_file())
print(temppath.exists())

with TemporaryDirectory() as d:
    print(d)
    temppath = Path(d)
    print(temppath.is_dir())
print(temppath.exists())

with TemporaryDirectory() as d, NamedTemporaryFile(dir=d) as f:
    print(d)
    print(f.name)
