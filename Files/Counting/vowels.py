import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'file.txt')

try:
    VOWELS = 'aeiouAEIOU'
    vowelCounter = 0
    with open(file_path) as f:
        for line in f:
            for char in line:
                if char in VOWELS:
                    vowelCounter += 1
        print(f'Vowels in this file: {vowelCounter}')


except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f'An error has occurred: {e}')