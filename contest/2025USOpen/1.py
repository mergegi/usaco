import sys
#sys.stdin = open("1.in")

from collections import defaultdict

N, M = [int(e) for e in input().strip().split()]

key = []

for _ in range(N):
    key.append(list(input().strip()))

loseSymbols = defaultdict(set)
for r in range(N):
    for c in range(r + 1):
        if key[r][c] == 'L':
            loseSymbols[r + 1].add(c + 1)
        elif key[r][c]  == 'W':
            loseSymbols[c + 1].add(r + 1)

# solve single match - print the output as well
# Input: one match from E: list of 2 elements: 1 for each play
def solveSingle(match):
    e1 = int(match[0])
    e2 = int(match[1])

    s1 = loseSymbols[e1]
    s2 = loseSymbols[e2]

    ws = s1.intersection(s2)

    w = len(ws)
    return (w * N * 2 - w * w)

for e in range(M):
    p1, p2 = [int(e) for e in input().strip().split()]
    print(solveSingle((p1,p2)))
