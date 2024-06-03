
import sys

def Addition(A,B):
    return A + B

def main():

    print("--------------------------------------------------")
    print("---------Automation to perform Addition-----------")
    print("--------------------------------------------------")

    if(len(sys.argv) == 2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This script used to perform addition of 2 integrl value")
            exit()
            
        if(sys.argv[1]=="--u" or sys.argv[1] == "--U"):
            print("Usag of the script : ")
            print("Name_of_File First_Argument Second_Argument")
            print("Note : Both the argument should be in the integral format")
            exit()
        else:
            print("Invalid option")
            print("Use --h option to get the help")
            print("Use --u option to get the Usage of application")

    if(len(sys.argv) == 3):
        try:
            ret = Addition(int(sys.argv[1]), int(sys.argv[2]))
            print("Addition is :  ",ret)
        
        except ValueError as obj1:
            print("Invalid type of arguments")

        except Exception as obj2:
            print("Unable to perform the task due to",obj2)

    else:
        print("Invalid option")
        print("Use --h option to get the help")
        print("Use --u option to get the Usage of application")

    print("--------------------------------------------------")
    print("---------Thank You for using our script-----------")
    print("------------created by Mahesh Pawar---------------")
    print("--------------------------------------------------")
 

if __name__ == "__main__":
    main()