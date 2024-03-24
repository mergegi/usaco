"""
ID: mfchen12
LANG: PYTHON3
TASK: ride
"""
def encode(name):
    code = 1
    for c in name:
        code *= (ord(c)- 64)
    code = code % 47
    return code

with open("ride.in", "r") as fIn, open("ride.out","w") as fOut:
    lines = fIn.readlines()

    cometName =  lines[0].strip()
    groupName =  lines[1].strip()

    cometCode = encode(cometName)

    groupCode=  encode(groupName)

    if cometCode == groupCode:
        fOut.write("GO\n")
    else:
        fOut.write("STAY\n")
