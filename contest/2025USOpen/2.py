import sys
#sys.stdin = open('2.in')

from collections import defaultdict

# read input
T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    h = [int(e) for e in input().strip().split()]

    hc = defaultdict(int)
    for i in h:
        hc[i] += 1

    hl = sorted(hc.keys())
    hl.reverse()
    K = hl[0]

    ans = 1 # add tallest
    for k, v in hc.items():
        if v >= 2: # if it's duplicated
            if k != K:
                ans += 2 # add 2: 1 on left, 1 on right

    print(ans)



