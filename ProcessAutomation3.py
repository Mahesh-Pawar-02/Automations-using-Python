import psutil

def CreateLog(FileName = "Marvellous.log"):
    fd = open(FileName,"w")

    separator = "-"*70

    fd.write(separator + "\n")
    fd.write("Marvellous Process Log" + "\n")
    fd.write(separator + "\n")

    fd.write("CONTENTS OF LOG FILR" + "\n")
    fd.write(separator + "\n")

    fd.close()

def main():
    CreateLog()

if __name__ == "__main__":
    main()