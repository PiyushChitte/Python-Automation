import os

def File_Write(filename):

    if(os.path.exists(filename)):
        print("Entre the data you want to write in file : ")
        Data = input()

        fd = open(filename, "a")
        fd.write(Data)
    else:
        print("File does not exists")
        return

def main():
    print("Entre the file you want to write : ")
    Name = input()

    File_Write(Name)


if __name__ == "__main__":
    main()