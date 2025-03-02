#import sys
#sys.stdin = open("2.in")

from collections import defaultdict

# read input
N, Q = [int(e) for e in input().strip().split()]

xRow = defaultdict(int)
yRow = defaultdict(int)
zRow = defaultdict(int)

ans =  0 

for _ in range(Q):
    x, y, z = [int(e) for e in input().strip().split()]
    # handle x row
    key = (y, z) #tuple
    xRow[key] += 1
    if xRow[key] == N: 
        ans += 1 

    # handle y row
    key = (x, z)
    yRow[key] += 1
    if yRow[key] == N: 
        ans += 1 

    # handle z row
    key = (x, y)
    zRow[key] += 1
    if zRow[key] == N: 
        ans += 1 
    
    print(ans)