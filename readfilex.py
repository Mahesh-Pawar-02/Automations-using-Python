import os

def main():

    print("Enter the name of file that you want to reading purpose : ")
    Fname = input()

    if os.path.exists(Fname):
        fobj = open(Fname, "r")
        print("File successfully opend in read mode")

        Data = fobj.read(10)
        print(Data)

        fobj.close()

    else:    
        print("Unable to open as file as file not present in current directory")
        
    
if __name__ == "__main__":
    main()