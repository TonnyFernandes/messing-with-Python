from random import randint as rd

# The usage of the sum() function would be better, in general.
def sumList(l):
    total = 0
    for x in range(0, len(l)):
        total += l[x]
    return total #return sum(l)

numbers = []
for x in range(50):
    numbers.append(int(rd(1, 25)))

print(numbers)
print(sumList(numbers))