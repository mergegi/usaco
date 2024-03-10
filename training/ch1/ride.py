with open("ride.in", "r") as fIn, open("ride.out","w") as fOut:
    lines = fIn.readlines()

    cometName =  lines[0].strip()
    groupName =  lines[1].strip()

    cometCode = 1
    for c in cometName:
            cometCode = cometCode * (ord(c)- 64)

    cometCode = cometCode % 47


    groupCode = 1
    for c in groupName: 
            groupCode = groupCode * (ord(c)- 64)
    
    groupCode = groupCode % 47

    if cometCode == groupCode:
        fOut.write("GO\n")
    else:
        fOut.write("STAY\n")
