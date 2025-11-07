data=[]

LUT = ""
lut_d = {}

lut = lut.split("\n")
for elem in lut:
    elem = elem.split(":")
    lut_d[int(elem[1], 16)] = chr(int(elem[0]))

flag = ""
for i in data:
    flag += lut_d[i]

print(flag)