# Design automation script which accept process name and display information of that process if it is running.
# Usage : ProcInfo.py Notepad

import sys
import logging
from Logger import CreateLog
from ProcessModule import DisplayProcess

def main():
    try:
        if(len(sys.argv) == 2):
            if((sys.argv[1]) == "--u" or (sys.argv[1]) == "--U"):
                print("Use the automation script as :")
                print("python ProcInfo_2.py --U or python ProcInfo_2.py -u")    
            elif((sys.argv[1]) == "--h" or (sys.argv[1]) == "--H"):
                print("This automation script display information of given running processes in the log file")
                print("Usage:\n python ProcInfo_2.py")
                print("For better usages please check --u flag")
            else:
                ProcessName = sys.argv[1]
                if ProcessName.strip() == "":
                    print("Process name cannot be empty.")
                    return
                CreateLog()
                logging.info("Application Started")
                DisplayProcess(ProcessName)
                logging.info("Application Finished")
    except Exception as e:
        logging.error(str(e))

if __name__ == "__main__":
    main() 