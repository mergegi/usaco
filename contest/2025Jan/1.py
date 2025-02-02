import sys
sys.stdin = open('1.in')

def solve(N, sky, A, B):
    res = 0
    if A == 0 and B == 0:
        for i in range(N):
            for j in range(N):
                if sky[i][j] == 'G' or sky[i][j] == 'B':
                    res += 1
        return res
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            pi = i - B
            pj = j - A
            if sky[i][j] == 'G':
                res += 1
                if pi < 0 or pj < 0:
                    continue
                elif sky[pi][pj] == 'G':
                    sky[pi][pj] = 'W'
                elif sky[pi][pj] == 'B':
                    sky[pi][pj] = 'G'
            elif sky[i][j] == 'B':
                res += 2
                if pi < 0 or pj < 0:
                    return -1
                elif sky[pi][pj] == 'W':
                    return -1
                elif sky[pi][pj] == 'G':
                    sky[pi][pj] = 'W'
                elif sky[pi][pj] == 'B':
                    sky[pi][pj] = 'G'
    return res

T = int(input().strip())

for _ in range(T):
    N, A, B = [int(e) for e in input().strip().split()]
    sky = []
    for i in range(N):
        line = input().strip()
        sky.append(list(line))
    print(solve(N, sky, A, B))