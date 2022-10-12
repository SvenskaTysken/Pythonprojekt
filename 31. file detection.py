import os

path = "C:\\Users\\46762\\Desktop\\Python.TXT"

if os.path.exists(path):
    print("File detected")
    if os.path.isfile(path):
        print("It is indeed a file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("File not found")