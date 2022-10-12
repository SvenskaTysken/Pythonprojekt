import os
import shutil

path = "folder"

try:
    #os.remove(path)
    #os.rmdir(path) #removedirectory
    shutil.rmtree(path) #delete a directory containing files
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("You don't have permission to delete that")
except OSError:
    print("You can't delete that using this function")
else:
    print(path+" was deleted")

