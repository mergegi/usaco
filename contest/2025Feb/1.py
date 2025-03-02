#import sys 
#sys.stdin = open('1.in')


# read input
N, U = [int(e) for e in input().strip().split()]

# canvas
C = []
for _ in range(N):
    C.append(list(input().strip()))

for i in range(N):
    for j in range(N):
        if C[i][j] == '.':
            C[i][j] = 0
        else:
            C[i][j] = 1

# operations
OP = []
for _ in range(U):
    OP.append( [int(e) - 1 for e in input().strip().split()] )

def solve():
    x = 0 
    qz = N // 2
    for i in range(qz):
        for j in range(qz):
            sum = C[i][j] + C[i][N - 1 - j] + C[N - 1 - i][j] + C[N - 1 - i][N - 1 - j]
            if sum == 1 or sum == 3:
                x += 1
            elif sum == 2:
                x += 2
    return x

ans = solve()
print(ans)

for i in range(U):
    sop = OP[i]
    m, n = sop

    bSum = C[m][n] + C[m][N - 1 - n] + C[N - 1 - m][n] + C[N - 1 - m][N - 1 - n]

    if C[m][n] == 0:
        C[m][n] = 1
    else:
        C[m][n] = 0

    aSum = C[m][n] + C[m][N - 1 - n] + C[N - 1 - m][n] + C[N - 1 - m][N - 1 - n]

    if bSum == 0 or bSum == 4:
        ans += 1
    elif bSum == 2:
        ans -= 1
    elif bSum == 1:
        if aSum == 0:
            ans -= 1
        elif aSum == 2:
            ans += 1
    elif bSum == 3:
        if aSum == 4:
            ans -= 1
        elif aSum == 2:
            ans += 1

    print(ans)