import os
from sys import *

def DirectoryWatcher(Dir_name):

    print("Current Directory is : "+Dir_name)

    path = Dir_name

    for foldername, subfolder, filenames in os.walk(path):  # topdown=False can be used to get from inside to outside
        print("Folder name is : "+foldername)
        for subf in subfolder:
            print("Subfolder name of "+foldername+" is "+subf)
        for fnames in filenames:
            print("File inside folder "+foldername+" is "+fnames+" having size "+ str(os.path.getsize(fnames)))
        print(" ")


def main():
    print("----------- Automation Script by Piyush Chitte ----------")
    print("Directory Watcher ")
    print("Current Script : "+argv[0])

    if(len(argv) >= 3):
        print("Invalid Arguments")

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This script will travel the directory and display all the entries of that directory")

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage: Application_name Directory_name")

    
    DirectoryWatcher(argv[1])


if __name__ == "__main__":
    main()