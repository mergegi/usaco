# simulation
#import sys
#sys.stdin = open('3.in')

# read input
N, K, T = [int(e) for e in input().strip().split()]
A = [int(e) for e in input().strip().split()]

cows = [i for i in range(N)]

def singleStep():
    prev = cows[A[0]]
    for i in range(K):
        tmp = cows[A[i]]
        cows[A[i]] = prev
        prev = tmp
    cows[A[0]] = prev 
    
    # advance active positions
    for i in range(K):
        A[i] = (1 + A[i]) % N


# write the solution using simulation 
for i in range(T):
    singleStep() # rotate once and advance

# write output
print(' '.join([str(c) for c in cows]))

for c in range(N):
    # calculate start time

    # calculate how many moves

    # calculate how far each move

    # move