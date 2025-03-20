import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'file.txt')

try:
    with open(file_path) as f:
        CONSONANTS = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
        consonantCounter = 0
        for line in f:
            for char in line:
                if char in CONSONANTS:
                    consonantCounter += 1
        
        print(f'Amount of consonsonants in the file: {consonantCounter}')
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f'An error has occurred: {e}')