from contextlib import closing

with closing(open("contextmanager.py")) as f:
    print(f.read())
