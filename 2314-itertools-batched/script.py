import json
import time
from itertools import batched
from urllib.request import urlopen

resp = urlopen("https://pypi.org/pypi/analytix/json")
versions = json.loads(resp.read())["releases"].keys()
latest = next(reversed(versions))

for batch in batched(versions, 5):
    for version in batch:
        print(f"Checking version {version}")
        resp = urlopen(f"https://pypi.org/pypi/analytix/{version}/json")
        ...

    if version != latest:
        print("Sleeping for ratelimits...")
        time.sleep(2)
