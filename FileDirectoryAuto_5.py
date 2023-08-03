# Write a program which accept 2 file names from user and compare both the files
from sys import *
import os 



def CompareString(filename):

    print("Entre the string you want to compare : ")
    Name = input()

    file = open(filename)
    data = file.read()

    occurrences = data.count(Name)
    print("Frequency of string in file is : ", occurrences)
    
   

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
        CompareString(argv[1])

    except Exception as E:
        print("Error: Invalid Input"+E)

if __name__ == "__main__":
    main()