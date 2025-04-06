#import sys
#sys.stdin = open("2.in")

from collections import defaultdict

N = int(input().strip())
a = [int(e) for e in input().strip().split()]

# unique number count up to a position
unique_count = [0] * N

s = set()

count = defaultdict(int)

for n in a:
    count[n] += 1

for i in range(N):
    unique_count[i] = len(s)
    s.add(a[i])

seen = defaultdict(int)

ans = 0
# loop backward
for i in range(N - 1, -1, -1):
    seen[a[i]] += 1
    if seen[a[i]] == 2: # cut point!!
        ans += unique_count[i] # how many unique numbers appeared before cut point
        if count[a[i]] > 2: # but if the cut point number also appeared before the cut point
            ans -= 1 # easy: just remove 1

print(ans)