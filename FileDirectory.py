import os

def Createfile(filename):

    if(os.path.exists(filename)):
        print("File is already existing")
        return
    else:
        fd = open(filename, "w")
print("File created sucessfully")

def File_Write(filename):

    if(os.path.exists(filename)):
        print("Entre the data you want to write in file : ")
        Data = input()

        fd = open(filename, "a")
        fd.write(Data)
    else:
        print("File does not exists")
        return

def Read_File(filename):

    if(os.path.exists(filename)):
        fd = open(filename, "r")
        Data = fd.read()
        print("Data from the file is ")
        print(Data)
    else:
        print("File does not exists")
        return

def Delete_File(filename):     

    if(os.path.exists(filename)):
        os.remove(filename)
        print("File is Deleted Successfully")
    else:
        print("File does not exists")
        return        


def main():
    print("---------- File Management Process by Piyush Chitte ----------")
    print("1. Create File")
    print("2. Write File")
    print("3. Read File")
    print("4. Delete File")

    option = int(input())

    match option:
        case 1:
            print("Entre the file name you want to create : ")
            Name = input()

            Createfile(Name)
        
        case 2:
            print("Entre the file you want to write : ")
            Name = input()

            File_Write(Name)

        case 3:
            print("Entre the file name you want to Read: ")
            Name = input()

            Read_File(Name)

        case 4:
            print("Entre the file you want to delete: ")
            Name = input()

            Delete_File(Name)

        case _:
            print("Invalid input")

    print("Do you want to continue?----y/n")
    Answer = input()

    if(Answer == "y"):
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Delete File")

        option = int(input())
        
    else:
        print("Thankyou for using Application")
        return



if __name__ == "__main__":
    main()