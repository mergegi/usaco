"""
ID: mfchen12
LANG: PYTHON3
TASK: beads
"""

# read input
with open("beads.in") as fIn:
    N = int(fIn.readline().strip())
    beads = fIn.readline().strip()

beads = beads + beads

# return the list of cut points
def findCutPoints():
    cutPoints = []
    for i in range(len(beads) - 1):
        if beads[i] != beads[i + 1]:
            cutPoints.append(i)
    return cutPoints


def collectLeft(cp):
    wCount = 0
    rCount = 0 
    bCount = 0
    for i in range(cp, 0, -1):
        if beads[i] == 'w':
            wCount += 1
        elif beads[i] == 'r':
            if bCount > 0:
                break
            else:
                rCount += 1
        elif beads[i] == 'b':
            if rCount > 0:
                break
            else: 
                bCount += 1
    return wCount + rCount + bCount

def collectRight(cp):
    wCount = 0
    rCount = 0 
    bCount = 0
    collectedCount = 0
    for i in range(cp + 1, len(beads), 1):
        if beads[i] == 'w':
            wCount += 1
        elif beads[i] == 'r':
            if bCount > 0:
                break
            else:
                rCount += 1
        elif beads[i] == 'b':
            if rCount > 0:
                break
            else: 
                bCount += 1
    return wCount + rCount + bCount

# find out all cutting point
cutPoints = findCutPoints()

# for every cutting point, simulate the process
maxBeadsCount = 0
for cp in cutPoints:
    beadsCount = collectLeft(cp) + collectRight(cp)
    if beadsCount > maxBeadsCount:
        maxBeadsCount = beadsCount

if maxBeadsCount == 0:
    maxBeadsCount = N

if maxBeadsCount > N:
    maxBeadsCount = N

with open("beads.out", "w") as fOut:
    fOut.write(f'{maxBeadsCount}\n')
