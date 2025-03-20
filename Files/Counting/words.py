import os
import string

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'file.txt')


try:
    with open(file_path, 'r') as f:

        content = f.read()
        content = content.translate(str.maketrans('', '', string.punctuation))

        words = content.split()

        print(f"Words in file: {len(words)}")
            
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f'An error has occurred: {e}')