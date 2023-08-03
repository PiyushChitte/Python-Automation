# Automation script which accept directory name and two file extension from user.
# Rename all files of first extension with second extension

import os
from sys import *

def ExtensionFinder(Dir_name):

    print("Enter the extension of files you want to search : ")
    ext = input()

    print("Entre the extension of file you want to change : ")
    ext1 = input()

    for foldername, subfolder, filenames in os.walk(Dir_name):
        for file in filenames:
            if file.endswith(ext):
                myfile = file
                base = os.path.splitext(myfile)[0]
                newfile = base + ext1
                print(os.name)
                os.rename(os.path.join(foldername,myfile), os.path.join(foldername, newfile))

        print("  ")



def main():

    print("----------- Automation Script by Piyush Chitte ----------")
    print("Directory Watcher and finding specific extension files ")
    print("Current Script : "+argv[0])

    if(len(argv) > 3):
        print("Invalid Arguments")

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This script will travel the directory and display all the entries of that directory")

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage: Application_name Directory_name")

    
    ExtensionFinder(argv[1])
 

if __name__ == "__main__":
    main()