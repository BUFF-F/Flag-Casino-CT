from FLAG_DATA import data as FLAG_DATA
from LUT_data import lut as LUT_DATA

lut_lines = LUT_DATA.split("\n")
lut_entries = []
for elem in lut_lines:
    parts = elem.split(":")
    lut_entries.append((int(parts[0]), parts[1].lower()))

lut_d = {int(v, 16): chr(k) for k, v in lut_entries}

flag = ""
for item in FLAG_DATA:
    s = item.lower()
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
            raise KeyError(f"No mapping for {item}")
    flag += ch

print(f"Generating Flag...\nFlag =\t\" {flag} \"")
