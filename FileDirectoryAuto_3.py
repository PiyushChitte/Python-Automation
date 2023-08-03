# Write a program which accept file name from user and create new file and copy all the data of previous file into new file
from sys import *
import os 
import shutil


def CopyFile(filename):

    fd = open("Demo.txt", "x")
    
    original = filename
    target = "Demo.txt"
    shutil.copy(original, target)

    print("Files are coppied successfully")


def main():
    print("---------- Automation Script by Piyush Chitte ----------")
    print("File Directory Procss")
    print("Current Directory: ",argv[0])

    if(len(argv)>= 3):
        print("Invalid Arguments")
        exit()

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage: Application_name File_name")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is for Checking particular file in a Directory")
        exit()

    try:
        CopyFile(argv[1])

    except Exception as E:
        print("Error: Invalid Input"+E)

if __name__ == "__main__":
    main()