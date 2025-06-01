import sys
#sys.stdin = open("3.in")

# Read input
N = int(input().strip())
a = [int(e) for e in input().strip().split()]
b = [int(e) for e in input().strip().split()]

count = 0 # without any operation, how many cows will be checked
for i in range(N):
    if a[i] == b[i]:
        count += 1

ans = [0] * (N + 1)
#ans[count] >= N

for c in range(N):
    # if there is one center
    newCount = count
    for i in range(N):
        #[c - i, c + 1]
        if c - i < 0 or c + i >= N:
            break
        if a[c - i] == b[c - i]:
            newCount -= 1
        if a[c + i] == b[c + i]:
            newCount -= 1 
        if a[c - i] == b[c + i]:
            newCount += 1 
        if a[c + i] == b[c - i]:
            newCount += 1
        ans[newCount] += 1

    # if there's no center (center with 2 point)
    newCount = count 
    for i in range(N):  # i is left point
        if c - i < 0 or c + i + 1 >= N:
            break
        if a[c - i] == b[c - i]:
            newCount -= 1
        if a[c + 1 + i] == b[c + 1 + i]:
            newCount -= 1
        if a[c - i] == b[c + 1 + i]:
            newCount += 1
        if a[c + 1 + i] == b[c - i]:
            newCount += 1
        ans[newCount] += 1

for a in ans:
    print(a)
    