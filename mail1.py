
import time
import urllib.error
import urllib.request
import smtplib
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_connected():
    try:
        urllib.request.urlopen('https://www.google.co.in/',timeout = 1)
        return True
    except urllib.error as err:
        return False
    
def MailSender():
    try:
        fromaddr = "try.web.new@gmail.com"
        toaddr = "ushap7497@gmail.com"
        # toaddr = "maheshpawar30627@gmail.com"
        # toaddr = "surawsekishor@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr

        body = """
        Hello....! 

        Greetings from Mahesh Pawar.
        
        This mail is auto generated by automation....... 

        Thanks & Regards,

        Mahesh Pawar
        +91 9322150275
        One step towards programming..
        """

        Subject = """
        Welcome from Mahesh Pawar
        """
        msg['Subject'] = Subject
        msg.attach(MIMEText(body,'plain'))
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(fromaddr,"qvbp xnrv pbcb pxaf")
        text = msg.as_string()
        s.sendmail(fromaddr,toaddr,text)
        s.quit()

        print("Successfully mail sent to ",(toaddr))

    except Exception as E:
        print("Unable to send mail",E)

    connected = is_connected()
 
    if connected:
        StartTime = time.time()
        MailSender()
        endTime = time.time()

        print("Took %s seconds to send email"%(endTime-StartTime))
    else:
        print("There is a no internet connection")

def main():
    print("--------------Created by Mahesh Pawar---------------")
    
    print("Application name is : "+argv[0])

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This script is used log record of running process")
        exit()

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Uage : Application_Name")
        exit()

    try:
        MailSender()

    except ValueError:
        print("ERROR : Invalid datatype of input")

    except Exception as e:
        print("ERROR : Invalid Input", e)

if __name__ == "__main__":
    main()