import sys
import logging
import re

from Logger import CreateDirectory
from Logger import CreateLogFile
from ProcessModule import DisplayProcessInformation
from MailModule import SendMail

def ValidateEmail(EmailID):
    """
    Validate email format using regular expression.
    """
    Pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    if re.match(Pattern, EmailID):
        return True
    else:
        return False


def main():
    try:
         if(len(sys.argv) == 2):
            if((sys.argv[1]) == "--u" or (sys.argv[1]) == "--U"):
                print("Use the automation script as :")
                print("python ProcInfoLog.py --U or python ProcInfoLog.py -u")    
            elif((sys.argv[1]) == "--h" or (sys.argv[1]) == "--H"):
                print("This automation script display information of given running processes in the log fil and send it over email")
                print("Usage:\n python ProcInfoLog.py <DirectoryName> <Email id>")
                print("For better usages please check --u flag")
            else:
                print("Invalid number of arguments")
         elif len(sys.argv) == 3:
                DirectoryName = sys.argv[1]
                EmailID = sys.argv[2]
                if DirectoryName.strip() == "":
                    print("Directory name cannot be empty.")
                    return
                if ValidateEmail(EmailID) == False:
                    print("Invalid Email Address")
                    return
                Status = CreateDirectory(DirectoryName)
                if Status == False:
                    return
                LogFile = CreateLogFile(DirectoryName)
                logging.info("****************************************************")
                logging.info("Automation Script Started")
                logging.info("****************************************************")
                DisplayProcessInformation()
                logging.info("Process information successfully stored.")
                SendMail(EmailID, LogFile)
                logging.info("Mail sent successfully to : {}".format(EmailID))
                logging.info("Automation Script Finished")
                logging.info("****************************************************")

    except KeyboardInterrupt:
        logging.error("Execution interrupted by user.")

    except Exception as e:
        logging.error("Exception : {}".format(str(e)))

if __name__ == "__main__":
    main()