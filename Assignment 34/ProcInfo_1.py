# Please follow below rules while designing automation script as
# • Accept input through command line or through file.
# • Display any message in log file instead of console.
# • For separate task define separate function.
# • For robustness handle every expected exception.
# • Perform validations before taking any action.
# • Create user defined modules to store the functionality.
# 1. Design automation script which display information of running processes as its name, PID,
# Username.
# Usage : ProcInfo.py

import sys
import logging
from Logger import CreateLog
from ProcessModule import DisplayProcessInformation

def main():
    try:
        if(len(sys.argv) == 2):
            if((sys.argv[1]) == "--u" or (sys.argv[1]) == "--U"):
                print("Use the automation script as :")
                print("python ProcInfo_1.py --U or python ProcInfo_1.py -u")    
            elif((sys.argv[1]) == "--h" or (sys.argv[1]) == "--H"):
                print("This automation script display information of running processes in the log file")
                print("Usage:\n python ProcInfo_1.py")
                print("For better usages please check --u flag")
            else:
                print("Unable to proceed as arguments are not matching")
                print("Please use --h or --u flag for getting more details")
        else:
            CreateLog()
            logging.info("Application Started")
            DisplayProcessInformation()
            logging.info("Application Finished")
    except Exception as e:
        logging.error(str(e))

if __name__ == "__main__":
    main()