import psutil
import time
import schedule
import os
import sys
import datetime

def CreateLog(Foldername = "Marvellous"):

    if not os.path.exists(Foldername):
        os.mkdir(Foldername)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")

    FileName = os.path.join(Foldername, "Marvellous%s.log" %(timestamp))
    
    fd = open(FileName,'w')

    separator = "-"*70

    fd.write(separator + "\n")
    fd.write("Marvellous Process Log" + "\n")

    fd.write("Log file created at : " + time.ctime() + "\n")
    fd.write(separator + "\n")

    Arr = GetProcessInfo()
    
    for data in Arr:
        fd.write("%s \n" %data)

    fd.write("CONTENTS OF LOG FILE" + "\n\n")
    fd.write(separator + "\n")


    fd.close()

def GetProcessInfo():
    listprocess = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        listprocess.append(proc.info)
    
    return listprocess

def main():
    print("Current time is ",datetime.datetime.now())
    schedule.every(int(sys.argv[1])).minutes.do(CreateLog)
    

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()