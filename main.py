import os
path = input('Please input the folder containing the content folder ')

with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file or entry.is_folder():
            print(entry.name)