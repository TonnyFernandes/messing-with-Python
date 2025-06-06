import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'file.txt')

def countLines(f):
    counter = 0
    for lines in f:
        counter += 1
    return counter

try:
    with open(file_path) as f:
        print(f'Lines in the file: {countLines(f)}')
except FileNotFoundError:
    print(f'The file {file_path} was not found')
except Exception as e:
    print(f'An error has occurred: {e}')