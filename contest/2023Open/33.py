# simulation
#import sys
import math
#sys.stdin = open('3.in')

# read input
N, K, T = [int(e) for e in input().strip().split()]
A = [int(e) for e in input().strip().split()]
A.append(N) # add dummy position of last cow position + 1

cows = [i for i in range(N)]

# for every cow, calculate the final position
for i in range(K):
    # A[i] i A[i + 1]
    for j in range(A[i], A[i + 1]):
        # j is the cows position
        startTime = j - A[i]
        distanceForOneMove = A[i + 1] - A[i]
        totalTime = T - startTime
        moveSteps = math.ceil(totalTime / distanceForOneMove)

        cows[(j + moveSteps * (A[i + 1] - A[i])) % N] = j

print(' '.join([str(c) for c in cows]))
