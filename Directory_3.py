# Automation script which accept two directory name from user
# Copy all files of first directory into second directory

import os
from sys import *
import subprocess
import shutil

def DirectoryWatcher(Dir_Name1, Dir_Name2):

    files = os.listdir(os.path.join(os.getcwd(),Dir_Name1))
    for file_name in files:
        print(file_name)

    path1 = os.path.join(os.getcwd(),Dir_Name2)
    print("path is: ",path1)
    #Dir_Name2 = os.mkdir(path1)

    #path2 = 
    
    shutil.copytree(os.path.join(os.getcwd(),Dir_Name1),path1)
    print("files copied successfully")

def main():
    print("Directory watcher application")

    if (len(argv) < 3):
        print("Insufficient arguments")
        exit()

    if(argv[1] == "-h"):
        print("This script will travel the directory and display the names of all entries")
        exit()

    if(argv[1] == "-u"):
        print("Usage: Application_name Directory_name")
        exit()

    DirectoryWatcher(argv[1],argv[2])

if __name__ == "__main__":
    main()
