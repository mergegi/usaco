"""
ID: mfchen12
LANG: PYTHON3
TASK: milk2
"""

milkingTimes = []

# read input

with open("milk2.in", "r") as fIn:
    N = int(fIn.readline().strip())
    for _ in range(N): 
        line = fIn.readline().strip() 
        timeRange = [int(word) for word in line.split()]
        milkingTimes.append(timeRange)

# sort
milkingTimes.sort()

#merge time range
mergedTimes = []

maxGap = 0

curS, curE = milkingTimes[0]

for i in range(1, N):
    s, e = milkingTimes[i]
    if s <= curE: #overlapping
        curE = max(curE, e)
    else: # not overlapping
        mergedTimes.append([curS, curE]) # finalize merging range
        maxGap = max(maxGap, s- curE)
        # start a new merging range
        curS = s
        curE = e
    
mergedTimes.append([curS, curE])

maxMilkingTime = 0
for s, e in mergedTimes:
    maxMilkingTime = max(maxMilkingTime, e - s)

#output
with open("milk2.out", "w") as fOut:
    fOut.write(f"{maxMilkingTime} {maxGap}\n")
