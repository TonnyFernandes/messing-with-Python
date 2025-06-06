# Apparently, if working with BIG numbers or if performance is key: use iteration or memoization instead
def factorial(n):
    if n in {0, 1}: return 1
    return factorial(n - 1) * n

while True:
    n = int(input('Enter a number: '))
    if n >= 1:
        print(factorial(int(n)))
        break
    print('The input must be a positive number')