import os

def main():

    print("Enter the name of file that you want to writing purpose : ")
    Fname = input()

    if os.path.exists(Fname):
        fobj = open(Fname, "a")
        print("File successfully opend in write mode")

        print("Enter the data that you want to write in file")
        Data = input()

        fobj.write(Data)

        fobj.close()

    else:    
        print("Unable to open as file as file not present in current directory")
        
    
if __name__ == "__main__":
    main()