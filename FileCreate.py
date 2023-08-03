import os

def Createfile(filename):

    if(os.path.exists(filename)):
        print("File is already existing")
        return
    else:
        fd = open(filename, "w")

def main():
    print("Entre the file name you want to create : ")
    Name = input()

    Createfile(Name)


if __name__ == "__main__":
    main()