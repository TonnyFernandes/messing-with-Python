I just learned how to read and write files thanks to this video:
    https://www.youtube.com/watch?v=Uh2ebFW8OYM

All I did differently was to ask DeepSeek on why I couldn't read/write my files. The result was the following lines:

import os

- script_dir = os.path.dirname(os.path.abspath(\_\_file\_\_))
- file_path = os.path.join(script_dir, 'file.txt')

- try:
    -    with open(file_path, 'r') as f:

~~Insert code here~~
- except FileNotFoundError:
    -    print(f"The file '{file_path}' was not found.")
- except Exception as e:
    -    print(f'An error has occurred: {e}')
