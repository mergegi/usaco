# calculate the nTH number in fibonacci sequence

def fibonacci(n):
    if n == 0:
        return 0 
    if n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
    

#print(fibonacci(6))