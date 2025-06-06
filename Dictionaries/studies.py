student = {'name': 'John', 'age': 25, 'courses': ['Math', 'Computer Science']}

print(student)
print(student['name'])

print(student.get('age'))
print(student.get('phone', 'Not found'))

student['phone'] = '555-5555'
print(student.get('phone', 'Not found'))

student['name'] = 'Jane'
print(student.get('name'))

student.update({'name': 'Tonny', 'age': 19, 'programming languages': ['C', 'JavaScript', 'Python']})
del student['courses']
age = student.pop('age')
print(student)
print(age)
print('\n')

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)