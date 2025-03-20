import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'file.txt')

try:
    with open(file_path) as f:
        NUMBERS = '0123456789'
        numberCounter = 0
        for line in f:
            for char in line:
                if char in NUMBERS:
                    numberCounter += 1
        print(f'Number of numbers in the file: {numberCounter}')
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f'An error has occurred: {e}')