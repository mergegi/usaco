def createFibSeq():
    a = 0
    b = 1 

    def nextFib():
        nonlocal a, b
        ret = a
        a, b = b, a + b
        return ret
    
    return nextFib

for _ in range(10):
    print(createFibSeq()())