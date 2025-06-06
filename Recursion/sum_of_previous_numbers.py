def sum(s):
    if s < 1: return 'Invalid input'
    if s == 1: return 1
    return s + sum(s-1)

num = int(input('Type a natural number: '))
print(sum(num))