#import sys
#sys.stdin = open("1.in")

T = int(input().strip())

for _ in range(T):
    S = input().strip()
    iS = int(S)

    if S[-1] == '0':
        print("E")
    else: 
        print("B")