def valueCounter(dictionary):
    counter = 0
    for keys in dictionary:
        if dictionary.values():
            counter += 1
    return counter

student = {'name': 'Tonny', 'birthday': [19, 8], 'languages': [['Portuguese', 'Native'], ['English', 'Advanced']]}
print(f'Values in dictionary: {valueCounter(student)}')