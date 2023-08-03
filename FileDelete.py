import os

def Delete_File(filename):     

    if(os.path.exists(filename)):
        os.remove(filename)
        print("File is Deleted Successfully")
    else:
        print("File does not exists")
        return        

def main():
    print("Entre the file you want to delete: ")
    Name = input()

    Delete_File(Name)

if __name__ == "__main__":
    main() 


