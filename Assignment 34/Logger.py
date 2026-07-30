import logging
import os
import datetime

def CreateLog():
    try:
        if not os.path.exists("Marvellous"):
            os.mkdir("Marvellous")
        fileName = f"ProcessLog_{datetime.datetime.now()}.log"
        logfile = os.path.join("Marvellous", fileName)
        logging.basicConfig(
            filename=logfile,
            level=logging.INFO,
            format="%(asctime)s : %(levelname)s : %(message)s",
            filemode='w')
        return logfile

    except Exception as e:
        print("Unable to create log file :", e)

def CreateDirectory(DirectoryName):
    try:
        if not os.path.exists(DirectoryName):
            os.mkdir(DirectoryName)
        return True
    except Exception as e:
        print("Unable to create directory :", e)
        return False

def CreateLogFile(DirectoryName):
    try:
        LogFile = os.path.join(DirectoryName, "ProcessLog.log")
        logging.basicConfig(
            filename=LogFile,
            level=logging.INFO,
            format="%(asctime)s : %(levelname)s : %(message)s",
            filemode="w"
        )
        return LogFile
    except Exception as e:
        print("Unable to create log file :", e)
