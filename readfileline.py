import os

def main():

    print("Enter the name of file that you want to reading purpose : ")
    Fname = input()

    if os.path.exists(Fname):
        fobj = open(Fname, "r")
        print("File successfully opend in read mode")

        str1 = fobj.readline()
        str2 = fobj.readline()
        str3 = fobj.readline()
        str4 = fobj.readline()

        print(str1)
        print(str2)
        print(str3)
        print(str4)
    
        fobj.close()

    else:    
        print("Unable to open as file as file not present in current directory")
        
    
if __name__ == "__main__":
    main()