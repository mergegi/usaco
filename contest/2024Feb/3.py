#import sys
#sys.stdin = open("3.in")

N, Q = [int(e) for e in input().strip().split()]
c = [int(e) for e in input().strip().split()]
t = [int(e) for e in input().strip().split()]

# difference between c and t
d = [c[i] - t[i] for i in range(N)]

d.sort(reverse=True)

for _ in range(Q):
    V, S = [int(e) for e in input().strip().split()]
    if d[V - 1] > S:
        print("YES")
    else:
        print("NO")



