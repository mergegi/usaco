#import sys
#sys.stdin = open("2.in")

# read input
N, M = [int(e) for e in input().strip().split()]
S = input().strip()
a = [int(e) for e in input().strip().split()]

def next(i):
    if i == N - 1:
        return 0
    else:
        return i + 1

def prev(i):
    if i == 0:
        return N - 1
    else:
        return i - 1

total = sum(a)
ans = total

# find losing point
for i in range(N):
    if S[i] == 'R' and S[next(i)] == 'L':
        # found losing point!!
        # need find how much it will lose!!
        # find possible losing milk from left side
        SR = 0 
        j = prev(i)
        while S[j] == 'R':
            SR += a[j]
            j = prev(j)
        ans -= min(SR, M)
        
        # do the same for right side
        SL = 0 
        j = next(next(i) + 1)
        while S[j] == 'L':
            SL += a[j]
            j = next(j)
        ans -= min(SL, M)

print(ans)

        