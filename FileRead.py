import os

def Read_File(filename):

    if(os.path.exists(filename)):
        fd = open(filename, "r")
        Data = fd.read()
        print("Data from the file is ")
        print(Data)
    else:
        print("File does not exists")
        return
    

def main():
    print("Entre the file name you want to Read: ")
    Name = input()

    Read_File(Name)


if __name__ == "__main__":
    main()