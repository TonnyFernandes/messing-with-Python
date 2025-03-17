def fibonacci(f):
    sequence = [0, 1]
    while len(sequence) < f:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

print(fibonacci(100))