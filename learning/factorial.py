# write a function to calculate factorial

# recursive
def factorial(n):
    if  n == 1: #base case
        return 1
    else: # sub case
        return n * factorial(n - 1)

# iterative
def factorial_WithLoop(n):
    res = 1
    while n >= 1:
            res = n * res
            n = n - 1

    return res

n = int(input('Factorial Number: '))
print(factorial_WithLoop(n))
#f5 = factorial(5)