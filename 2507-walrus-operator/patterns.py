import re

pattern1 = re.compile(r"[0-9]+")
pattern2 = re.compile(r"[A-Za-z]+")

data = "Hello world"

if match1 := pattern1.match(data):
    result = match1.group(1)
elif match2 := pattern2.match(data):
    result = match2.group(2)
else:
    result = None
