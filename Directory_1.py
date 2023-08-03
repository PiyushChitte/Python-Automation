# Automation script which accept directory name and file extension from user.
# Display all files with that extension

import os
from sys import *

def ExtensionFinder(Dir_name):

    print("Enter the extension of files you want to search : ")
    ext = input()

    for foldername, subfolder, filenames in os.walk(Dir_name):
        for file in filenames:
            if file.endswith(ext):
                print(os.path.join(foldername, file))
            else:
                print("No such file found")
                exit()


def main():

    print("----------- Automation Script by Piyush Chitte ----------")
    print("Directory Watcher and finding specific extension files ")
    print("Current Script : "+argv[0])

    if(len(argv) >= 3):
        print("Invalid Arguments")

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This script will travel the directory and display all the entries of that directory")

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage: Application_name Directory_name")

    
    ExtensionFinder(argv[1])


if __name__ == "__main__":
    main()