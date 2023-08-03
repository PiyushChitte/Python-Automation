 from sys import *
import os
import hashlib

def hashfile(path,blocksize = 1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def DisplayChecksum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    exists = os.path.isdir(path)

    if exists:
        for dirName,subdir,fileList in os.walk(path):
            print("Current folder is: "+dirName)
            for file in fileList:
                path = os.path.join(dirName,file)
                file_hash = hashfile(path)
                print(path)
                print(file_hash)
                print(' ')
    else:
        print("Invalid path")


def main():

    print("----------- Automation Script by Piyush Chitte ----------")
    print("Directory Watcher and finding specific extension files ")
    print("Current Script : "+argv[0])

    if(len(argv) != 2):
        print("Invalid Arguments")

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This script will travel the directory and display all the entries of that directory")

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage: Application_name Directory_name")

    
    try:
        arr = DisplayChecksum(argv[1])
    except ValueError:
        print("Error: Invalid datatype of input")
    except Exception as E:
        print("Error: Invalid input",E)


if __name__ == "__main__":
    main()