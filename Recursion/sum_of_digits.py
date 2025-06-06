def sum_digits(x):
    if x < 10: return x
    return (x % 10) + sum_digits(int(x / 10))

num = int(input('Type an intenger: '))
print(f"Sum of digits: {sum_digits(num)}")