
import sys

def Addition(A,B):
    return A + B

def main():

    print("--------------------------------------------------")
    print("---------Automation to perform Addition-----------")
    print("--------------------------------------------------")

    if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
        print("This script used to perform addition of 2 integrl value")
        exit()
        
    if(sys.argv[1]=="--u" or sys.argv[1] == "--U"):
        print("Usag of the script : ")
        print("Name_of_File First_Argument Second_Argument")
        print("Note : Both the argument should be in the integral format")
        exit()

    ret = Addition(int(sys.argv[1]), int(sys.argv[2]))
    print("Addition is :  ",ret)

if __name__ == "__main__":
    main()