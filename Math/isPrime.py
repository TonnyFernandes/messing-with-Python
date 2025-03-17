from math import sqrt

def isPrime(x):

    # 2 is the only even prime number, so let's take it out of the way
    if x==2:
        return True
    
    # By definition, negative numbers and the number 1 are NOT prime. Also, this removes even numbers
    if x<2 or x%2==0:
        return False
    
    i = 3
    # If x is divided by ANY of the numbers from x to the square root to x, it's not a prime
    while i <= sqrt(x):
        if x%i==0:
            return False
        i += 2

    # If x reached this far, it means it's a prime number
    return True

for x in range(0, 1000):
    if(isPrime(x)):
        print(x)
