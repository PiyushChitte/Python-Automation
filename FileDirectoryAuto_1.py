# Write a program which accepts file name from user and check whether that file exists in current directory or not
from sys import *
import os 


def CheckFile(filename):

    fd = os.path.exists(filename)

    if(fd == True):
        print("File name : "+filename)
        print("File exists in the Current Directory")
    else:
        print("File name : "+filename)
        print("File does not exists")



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
        CheckFile(argv[1])

    except Exception as E:
        print("Error: Invalid Input"+E)

if __name__ == "__main__":
    main()