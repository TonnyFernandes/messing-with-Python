def keyCounter(dictionary):
    counter = 0
    for keys in dictionary:
        counter += 1
    return counter

student = {'name': 'Tonny', 'birthday': [19, 8], 'languages': [['Portuguese', 'Native'], ['English', 'Advanced']]}
print(f'Keys in dictionary: {keyCounter(student)}')