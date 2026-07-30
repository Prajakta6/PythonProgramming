# Design automation script which accept directory name from user and create log file in that directory which contains information of running processes as its name, PID, Username.
# Usage: ProcInfoLog.py Demo
# Demo is name of Directory.

import sys
import logging
from Logger import CreateDirectory
from Logger import CreateLogFile
from ProcessModule import DisplayProcessInformation

def main():
    try:
        if(len(sys.argv) == 2):
            if((sys.argv[1]) == "--u" or (sys.argv[1]) == "--U"):
                print("Use the automation script as :")
                print("python ProcInfo_3.py --U or python ProcInfo_3.py -u")    
            elif((sys.argv[1]) == "--h" or (sys.argv[1]) == "--H"):
                print("This automation script display information of given running processes in the log file")
                print("Usage:\n python ProcInfo_3.py Demo")
                print("For better usages please check --u flag")
            else:
                DirectoryName = sys.argv[1]
                if DirectoryName.strip() == "":
                    print("Directory name cannot be empty.")
                    return
                Status = CreateDirectory(DirectoryName)
                if Status == False:
                    return
                CreateLogFile(DirectoryName)
                logging.info("Application Started")
                DisplayProcessInformation()
                logging.info("Application Finished")

    except Exception as e:
        logging.error(str(e))

if __name__ == "__main__":
    main()