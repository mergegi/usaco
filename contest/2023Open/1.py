#import sys
#sys.stdin = open('1.in')

# read input
N = int(input().strip())
S = input().strip()

# states
MinE = 0 # min excitement num
MaxE = 0 # max excitement num
lastNonFL = None # last non F letter
fCount = 0 # F count in a pattern
pattern = None

# patterns 
'''
"NF" - no F
"BFB" 
"BFE"
"EFE"
"EFB"
"FF"
"FB"
"FE"
"BF"
"EF"
'''

# initialize state based on first letter
if S[0] == "F":
    pattern = "FF"
    fCount = 1
else:
    pattern = "NF"
    lastNonFL = S[0]

# scan each letter from the second one and update the pattern.
for i in range(1, N):
    if S[i] == 'F':
        fCount += 1
        if pattern == 'NF':
            if lastNonFL == 'B':
                pattern = 'BF'
            if lastNonFL == 'E':
                pattern = 'EF'
    elif S[i] == 'B':
        if pattern == 'NF':
            if lastNonFL == 'B':
                MinE += 1
                MaxE += 1
        elif pattern == 'FF':
            MaxE += fCount
        elif pattern == 'BF':
            MaxE += (fCount + 1)
            if fCount % 2 == 0:
                MinE += 1
        elif pattern == 'EF':
            MaxE += fCount
            if fCount % 2 != 0:
                MinE += 1

        fCount = 0
        pattern = 'NF'
        lastNonFL = 'B'

    elif S[i] == 'E':
        if pattern == 'NF':
            if lastNonFL == 'E':
                MinE += 1
                MaxE += 1
        elif pattern == 'FF':
            MaxE += fCount
        elif pattern == 'EF':
            MaxE += (fCount + 1)
            if fCount % 2 == 0:
                MinE += 1
        elif pattern == 'BF':
            MaxE += fCount
            if fCount % 2 != 0:
                MinE += 1

        fCount = 0
        pattern = 'NF'
        lastNonFL = 'E'

# update MinE and MaxE if last letter is F
if S[-1] == 'F':
    MaxE += fCount

if pattern == 'FF':
    MaxE -= 1

# now we find out MinE and MaxE
if S[0] == 'F' or S[-1] == 'F':
    step = 1
else:
    step = 2 # 2, 4, 6

count = (MaxE - MinE) // step + 1

# print result
print(count)
for i in range(count):
    print(MinE + step * i)

