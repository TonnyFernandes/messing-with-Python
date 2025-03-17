def isPrime(x):
    if x==1:
        return False
    i = 2
    while i<x:
        if x%i==0:
            return False
        i+=1
    return True

for x in range(1, 101):
    if isPrime(x):
        print(x)
