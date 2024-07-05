import json
from timeit import repeat

import toml
import yaml
from tabulate import tabulate

N = 1000

with open("benchmarks/data/analytix.json") as f:
    json_text = f.read()
    json_data = json.loads(json_text)

with open("benchmarks/data/analytix.toml") as f:
    toml_text = f.read()
    toml_data = toml.loads(toml_text)

with open("benchmarks/data/analytix.yaml") as f:
    yaml_text = f.read()
    yaml_data = yaml.safe_load(yaml_text)

tests = [
    # JSON
    {
        "msgspec.json.decode(data)": {"setup": "import msgspec", "data": json_text},
        "json.loads(data)": {"setup": "import json", "data": json_text},
    },
    {
        "msgspec.json.encode(data)": {"setup": "import msgspec", "data": json_data},
        "json.dumps(data)": {"setup": "import json", "data": json_data},
    },
    {
        "msgspec.json.decode(data)": {"setup": "import msgspec", "data": json_text},
        "orjson.loads(data)": {"setup": "import orjson", "data": json_text},
    },
    {
        "msgspec.json.encode(data)": {"setup": "import msgspec", "data": json_data},
        "orjson.dumps(data)": {"setup": "import orjson", "data": json_data},
    },
    # TOML
    {
        "msgspec.toml.decode(data)": {"setup": "import msgspec", "data": toml_text},
        "toml.loads(data)": {"setup": "import toml", "data": toml_text},
    },
    {
        "msgspec.toml.decode(data)": {"setup": "import msgspec", "data": toml_text},
        "tomllib.loads(data)": {"setup": "import tomllib", "data": toml_text},
    },
    {
        "msgspec.toml.encode(data)": {"setup": "import msgspec", "data": toml_data},
        "toml.dumps(data)": {"setup": "import toml", "data": toml_data},
    },
    # YAML
    {
        "msgspec.yaml.decode(data)": {"setup": "import msgspec", "data": yaml_text},
        "yaml.load(data, Loader=yaml.Loader)": {
            "setup": "import yaml",
            "data": yaml_text,
        },
    },
    {
        "msgspec.yaml.decode(data)": {"setup": "import msgspec", "data": yaml_text},
        "yaml.load(data, Loader=yaml.CLoader)": {
            "setup": "import yaml",
            "data": yaml_text,
        },
    },
    {
        "msgspec.yaml.encode(data)": {"setup": "import msgspec", "data": yaml_data},
        "yaml.dump(data, Dumper=yaml.Dumper)": {
            "setup": "import yaml",
            "data": yaml_data,
        },
    },
    {
        "msgspec.yaml.encode(data)": {"setup": "import msgspec", "data": yaml_data},
        "yaml.dump(data, Dumper=yaml.CDumper)": {
            "setup": "import yaml",
            "data": yaml_data,
        },
    },
]

table = []

for test in tests:
    times = []
    for name, meta in test.items():
        print(f"Running benchmark '{name}'...", end=" " * 10 + "\r", flush=True)
        times.append(
            min(
                repeat(
                    name,
                    setup=meta["setup"],
                    globals={"data": meta["data"]},
                    number=N,
                )
            )
            / N
            * 1e6
        )

    table.append((name, times[1], times[0], times[1] / times[0]))


print(
    tabulate(
        table,
        headers=["Test", "Run (μs)", "Msgspec (μs)", "Speedup (x)"],
        floatfmt=",.1f",
    )
)
