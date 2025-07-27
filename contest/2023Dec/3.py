#import sys
import math
#sys.stdin = open('3.in')

# read input
T = int(input().strip())

def solve(N, h, a, t):
    combo = list(zip(t, h, a))

    # sort it by t
    combo.sort(reverse=True)

    # for each pair of plants next to each other
    # find the longest days that satisfy the required order
    ld = 0 
    for i in range(0, N-1):
        # combo[i + 1] combo[i]
        shorter = combo[i]
        longer = combo[i + 1]
        y = longer[1]
        x = shorter[1]
        rx = shorter[2]
        ry = longer[2]
        if rx == ry:
            if x < y:
                d = 0 
            else:
                return - 1
        else:
            d = math.ceil((x - y) / (ry - rx))
            if (x - y) % (ry - rx) == 0:
                d += 1
        ld = max(ld, d)

    # verify using the longest days for each pair of plants
    for i in range(0, N - 1):
        # combo[i - 1] combo[i]
        shorter = combo[i]
        longer = combo[i + 1]
        y = longer[1]
        x = shorter[1]
        rx = shorter[2]
        ry = longer[2]

        if x + ld * rx >= y + ld * ry: # it doesn't work!!
            return - 1
        
    return ld

for _ in range(T):
    N = int(input().strip())
    h = [int(e) for e in input().strip().split()]
    a = [int(e) for e in input().strip().split()]
    t = [int(e) for e in input().strip().split()]

    print(solve(N, h, a, t))
