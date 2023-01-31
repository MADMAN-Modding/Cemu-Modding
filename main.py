import os

import shutil

path = input('Please input the folder containing the content folder ')

with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)

base = input('Base Game Dump ')

with os.scandir(base) as it:
    for base in it:
        if not base.name.startswith('.') and base.is_file ():
            os.stat(entry.name)== os.stat(base.name)
            shutil.copy(entry.name,base.name)
        print(base.name)
            
