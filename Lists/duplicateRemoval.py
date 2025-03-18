from random import randint as rd

def duplicateRemoval(myList):
    mySet = set(myList)
    uniqueList = list(mySet)
    return uniqueList

myList = []
for x in range(100):
    myList.append(rd(1, 100))

print(duplicateRemoval(myList))