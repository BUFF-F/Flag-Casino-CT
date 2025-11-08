from data import data
from lut import lut

lut_d = {}

lut = lut.split("\n")

lut_entries = []
for elem in lut:
    parts = elem.split(":")
    lut_entries.append((int(parts[0]), parts[1].lower()))

lut_d = {int(v, 16): chr(k) for k, v in lut_entries}

flag = ""

for i in data:
    s = i.lower()
    key = int(s, 16)
    if key in lut_d:
        ch = lut_d[key]
    else:
        ch = None
        for k, v in lut_entries:
            if v.endswith(s):
                ch = chr(k)
                break
        if ch is None:
            raise KeyError(f"No mapping for {i}")
    flag += ch

print(flag)
