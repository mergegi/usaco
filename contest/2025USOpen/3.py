import sys
#sys.stdin = open('3.in')

# read input
N, Q = [int(e) for e in input().strip().split()]
s = input().strip()

first_m_lookups = []
last_o_lookups = []

for i in range(26):
    ch = chr(ord('a') + i)

    lu = [-1] * N
    cur = -1
    for j in range(N - 1, -1, -1):
        if s[j] != ch:
            cur = j 
        lu[j] = cur
    first_m_lookups.append(lu)

    lu = [-1] * N 
    cur = -1
    for j in range(N): 
        if s[j] == ch:
            cur = j

def solve(l, r):
    ans = -1
    # bruteforce 26 letters  [moo]
    for i in range(26):
        ch = chr(ord('a') + i) # for moo with this ch as 'o'
        
        # find 'm' - first letter in moo pattern
        first = -1
        for j in range(l, r + 1):
            if s[j] != ch:
                first = j
                break
        if first == -1:
            continue
        
        # find last 'o'
        last = -1
        for j in range(r, l - 1, -1):
            if s[j] == ch:
                last = j
                break
        if last == -1:
            continue
        
        if last < first + 2:
            continue
        
        # try middle one - another brute force
        for j in range(first + 1, last):
            if s[j] == ch:
                ans = max(ans, (last - j) * (j - first))
                
    return ans
        
        

for _ in range(Q):
    l, r = [int(e) -  1 for e in input().strip().split()]
    print(solve(l, r))