import os


# This part will copy the text file
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'Files', 'file.txt')
fileCopy_path = os.path.join(script_dir, 'Files', 'copy.txt')
# This time, I need to create another path for my, yet to be created, copy
# By using the " 'Files', 'file.txt' " bit, I created a path to my subdirectory 'Files'

try:
    with open(file_path, 'r') as rf:
        with open(fileCopy_path, 'w') as wf:
            # for line in rf:
            # wf.write(line)
            # Would be good if the file was BIG, but it isn't the case. So instead I will use this:
            print('Copying the .txt')
            wf.write(rf.read())
            print('Copy complete. Check the Files folder')
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f'An error has occurred: {e}')



# Now, let's copy the picture
drive_path = os.path.join(script_dir, 'Files', 'drive.jpg')
copyDrive_path = os.path.join(script_dir, 'Files', 'copy.jpg')

try:
    with open(drive_path, 'rb') as rf:
        with open(copyDrive_path, 'wb') as wf:
            print('Copying the .jpg')
            chunk_size = 4096
            rf_chunk = rf.read(chunk_size)
            while len(rf_chunk) > 0:
                wf.write(rf_chunk)
                rf_chunk = rf.read(chunk_size)
            print('Copy complete. Check the Files folder')

except FileNotFoundError:
    print(f"The file '{drive_path}' was not found.")
except Exception as e:
    print(f'An error has occurred: {e}')
