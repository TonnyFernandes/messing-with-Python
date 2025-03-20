import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'file.txt')

try: 
    with open(file_path, 'w') as f:
        t = input('Type anything: ')
        print('Now check the folder this script is in')
        f.write(t)
        #   If I use seek, I can overwrite what was written:
        f.seek(0)
        f.write(' ')
        # This erases what the first character was
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f'An error has occurred: {e}')