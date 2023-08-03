# Below is the for Automation Scripts

import sys

def fun(parameter):
    # Logic of Script

def main():
    print("------------ Automation Script by Piyush Chitte -------------")
    print("Application name : "+sys.argv[0])

    if(len(argv) != 3):
        print("Error : Invalid nummber of Arguments")
        exit()

    if (argv[1] == "-h"):
        print("This script is designed for ____________")
        exit()

    if (argv[1] == "-u"):
        print("Usage : Application_Name ___________")
        exit()
    
    try:
        fun(argv[1])

    except Exception as E:
        print("Error : Invalid input"+E)

    if((len(argv)< 1) or (len(argv) > 3)):
        print("Error : Invalid number of arguments")

if __name__ == "__main__":
    main()