import msgspec

# json.dumps

d = {"a": "1", "b": "2"}

with open("output.msgpack", "wb") as f:
    f.write(msgspec.msgpack.encode(d))

with open("output.json", "rb") as f:
    print(msgspec.json.decode(f.read()))
