#import sys
#sys.stdin = open("mopinion.in")

def solve(N,cows):
    if N == 2:
        if cows[0] == cows[1]:
            return [cows[0]]
        else:
            return [-1]
    majority = set()
    for i in range(N - 2):
        if cows[i] == cows[i + 1]:
            majority.add(cows[i])
        elif cows[i] == cows[i + 2]:
            majority.add(cows[i])
        elif cows[i + 1] == cows[i + 2]:
            majority.add(cows[i + 1])

    if len(majority) == 0:
        return[-1]
    
    return sorted(list(majority))

# read input
T = int(input().strip())

for i in range(T):
    N = int(input().strip())
    cows = [int(i) for i in input().strip().split()]
    sol = solve(N, cows)
    print(' '.join([str(e) for e in sol]))