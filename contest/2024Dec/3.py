#import sys
from collections import defaultdict
#sys.stdin = open("3.in")

N, F = [int(e) for e in input().strip().split()]
con = input().strip()

def isMoo(tri):
    if tri[1] == tri[2] and tri[0] != tri[1]:
        return True
    return False

def findAnswer(inStr):
    # a set of 'moo' satisfy the condition

    mem = defaultdict(int)

    for i in range(N - 2):
        tri = inStr[i:i + 3]
        if isMoo(tri):
            mem[tri] += 1 

    ans = set()
    for k, v in mem.items():
        if v >= F:
            ans.add(k)
        
        # if the character at i is changed, return the new moo pattern
    def findNewMoo(i):
        nonlocal mem, ans
        oldMoo = set()
        ret = set()
        # situation _xx
        if i < N - 2:
            oriMoo = con[i: i + 3]
            if isMoo(oriMoo):
                oldMoo.add(oriMoo)
            for j in range(ord('a'), ord('z') + 1):
                c = chr(j)
                if c != con[i]: 
                    can = c + con[i + 1: i + 3]
                    if isMoo(can):
                        ret.add(can)

        # situation x_x
        if i < N - 1 and i > 0:
            oriMoo = con[i - 1: i + 2]
            if isMoo(oriMoo):
                oldMoo.add(oriMoo)
            for j in range(ord('a'), ord('z') + 1):
                c = chr(j)
                if c != con[i]: 
                    can = con[i - 1] + c + con[i + 1]
                    if isMoo(can):
                        ret.add(can)

        # situation xx_
        if i > 1:
            oriMoo = con[i - 2 : i + 1]
            if isMoo(oriMoo):
                oldMoo.add(oriMoo)
            for j in range(ord('a'), ord('z') + 1):
                c = chr(j)
                if c != con[i]: 
                    can = con[i - 2: i] + c
                    if isMoo(can):
                        ret.add(can)
        ret = ret - oldMoo
        return ret

    for i in range(N):
        nm = findNewMoo(i)
        for m in nm:
            if mem[m] == F - 1:
                ans.add(m)

    return ans


finalAns = findAnswer(con)

finalAns = sorted(finalAns)

print(len(finalAns))
for e in finalAns:
    print(e)