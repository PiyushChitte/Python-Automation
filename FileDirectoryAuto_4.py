# Write a program which accept 2 file names from user and compare both the files
from sys import *
import os 
import filecmp


def CompareFile(filename1, filename2):

    compare = filecmp.cmp(filename1, filename2)

    if(compare == True):
        print("Both the files are equal")
    else:
        print("Files are not equal")
   

def main():
    print("---------- Automation Script by Piyush Chitte ----------")
    print("File Directory Procss")
    print("Current Directory: ",argv[0])

    if(len(argv)>= 4):
        print("Invalid Arguments")
        exit()

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage: Application_name File_name")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is for Checking particular file in a Directory")
        exit()

    try:
        CompareFile(argv[1] and "Demo.txt")

    except Exception as E:
        print("Error: Invalid Input"+E)

if __name__ == "__main__":
    main()