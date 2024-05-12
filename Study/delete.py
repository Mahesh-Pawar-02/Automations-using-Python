import os

def main():

    print("Enter the name of file that you want to delete : ")
    Fname = input()

    if os.path.exists(Fname):
        os.remove(Fname)

        print("File successfully deleted")

    else:    
        print("Unable to delete as file as file not present in current directory")
        
    
if __name__ == "__main__":
    main()