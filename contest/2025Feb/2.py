#import sys 
#sys.stdin = open('2.in')

N = int(input().strip())
a = [int(e) for e in input().strip().split()]

times = [0] * (N + 1)
for n in a:
    times[n] += 1


op1 = 0
for i in range(N + 1):
    ans = 0
    mex = i
    
    if times[mex] > op1:
        ans = times[mex]
    else:
        ans = op1
    
    if times[mex] == 0:
        op1 += 1
    
    print(ans)