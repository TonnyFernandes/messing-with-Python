import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'file.txt')

try:
    with open(file_path, 'r') as f:
        # Read all at once. Good for small files
        # print (f.read())

        # Read line to line. Good for larger files
        # for line in f:
        #     print(line, end='')

        # Read chunks of the text
        # size_to_read = 10
        # f_content = f.read(size_to_read)
        # print(f.tell())
        # while len(f_content) > 0:
        #     print(f_content, end='*')
        #     f_content = f.read(size_to_read)
            
        # Manipulate where will the code read the file
        size_to_read = 10

        f_content = f.read(size_to_read)
        print(f_content, end='')

        f.seek(0) # This sets the reading to the beggining

        f_content = f.read(size_to_read)
        print(f_content)
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f'An error has occurred: {e}')