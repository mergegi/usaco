#import sys
#sys.stdin = open("1.in")

def round(n, d): # n is the number to be rounded. d is the number rounded to (such as 10, 100, 1000, 10000....)
    if n % d < d // 2:
        return n - n % d
    else: 
        return n + d - n % d

def chain_round(n, d):
    ten = 10 
    while ten <= d:
        n = round(n, ten)
        ten *= 10
    return n

T = int(input().strip())

for i in range(T): 
    N = int(input().strip())
    v = 0 
    for i in range(2, N + 1):
        ten = 10
        while ten < i:
            ten *= 10

        if round(i, ten) != chain_round(i, ten):
            v += 1
    print(v)