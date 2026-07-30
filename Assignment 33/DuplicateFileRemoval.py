import sys
import os
import hashlib
import datetime
import time
import schedule
import smtplib
from email.message import EmailMessage
from email_validator import validate_email, EmailNotValidError

def Check_Email(email):
    try:
        # Check syntax and deliverability (DNS lookup)
        email_info = validate_email(email, check_deliverability=True)
        
        # Get normalized email address
        normalized_email = email_info.normalized
        return f"Valid email: {normalized_email}"
        
    except EmailNotValidError as e:
        # Returns a human-readable explanation of why it failed
        return f"Invalid email: {str(e)}"

def CalculateChecksum(FileName):
    fObj = open(FileName, "rb") 
    hObj = hashlib.md5()
    Buffer = fObj.read(1024)
    while(len(Buffer) > 0):
        hObj.update(Buffer)
        Buffer = fObj.read(1024)
    fObj.close()
    return hObj.hexdigest()

def FindDuplicate(DirectoryName):
    Ret = False
    Ret = os.path.exists(DirectoryName)

    if Ret == False:
        print("Path is invalid!")
        return
    
    Ret = os.path.isdir(DirectoryName)
    if Ret == False:
            print("It is not a Directory")
            return
    
    Duplicate = {}

    for FolderName, SubFolder, Filename in os.walk(DirectoryName):
        for fName in Filename:
            fName = os.path.join(FolderName,fName)
            Checksum = CalculateChecksum(fName)
            if Checksum in Duplicate:
                Duplicate[Checksum].append(fName)
            else:
                Duplicate[Checksum] = [fName]

    return Duplicate

def DeleteDuplicate(DirectoryName, ReceiverEmail):
    Ret = os.path.exists(DirectoryName)
    if Ret == True:
        Ret = os.path.isdir(DirectoryName)
        if(Ret == False):
            print("Unable to proceed as directory name is existing but it's not a directory.")
            return
    else:
        os.mkdir(DirectoryName)
        print("Directory for the logfile gets created successfully.")

    Check_Email(ReceiverEmail)
    Scanning_StartTime = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    MyDict = FindDuplicate(DirectoryName)
    Result = list(filter((lambda x: len(x) > 1), MyDict.values()))
    Scanning_CompletionTime = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    NameOfDirectoryScanned = DirectoryName
    TotalNumberOfFilesScanned = len(MyDict.values())
    TotalNumberOfDuplicateFilesFound = Result
    ChecksumValuesOfDuplicateFiles = MyDict.keys()
    Count = 0
    TotalDeleted = 0

    for values in Result:
        for subValue in values:
            Count = Count + 1
            if Count > 1:
                os.remove(subValue)
                TotalDeleted = TotalDeleted + 1
        Count = 0     

    print("Total deleted files : ", TotalDeleted)   
    CreateLogDirectory(Scanning_StartTime, Scanning_CompletionTime,  NameOfDirectoryScanned, TotalNumberOfFilesScanned, TotalNumberOfDuplicateFilesFound, ChecksumValuesOfDuplicateFiles, TotalDeleted, ReceiverEmail)

def CreateLogDirectory(Scanning_StartTime, Scanning_CompletionTime, NameOfDirectoryScanned, TotalNumberOfFilesScanned, TotalNumberOfDuplicateFilesFound, ChecksumValuesOfDuplicateFiles, TotalDeleted, ReceiverEmail):
    try:
        current_datetime = datetime.datetime.now()

        timestamp = current_datetime.strftime("%d_%m_%Y_%H_%M_%S")
        log_filename = f"DuplicateRemovalLog_{timestamp}.log"

        if not os.path.exists("Marvellous"):
            os.makedirs("Marvellous")

        destination_path = os.path.join("Marvellous", log_filename)
        log_message = (
            f"Starting time of directory scanning: {Scanning_StartTime}\n"
            f"Completion time of directory scanning: {Scanning_CompletionTime}\n"
            f"Name of the directory scanned: {NameOfDirectoryScanned}\n"
            f"Total number of files scanned: {TotalNumberOfFilesScanned}\n"
            f"Total number of duplicate files found: {TotalNumberOfDuplicateFilesFound}\n"
            f"Checksum values of duplicate files: {ChecksumValuesOfDuplicateFiles}\n"
            f"Total number of duplicate files deleted: {TotalDeleted}\n")

        log_file = open(destination_path, "a")
        log_file.write(log_message)
        Send_mail(destination_path, ReceiverEmail, Scanning_StartTime, Scanning_CompletionTime, NameOfDirectoryScanned, TotalNumberOfFilesScanned, TotalNumberOfDuplicateFilesFound, TotalDeleted)

    except Exception as e:
        print("Error:", e)

# --------------------------------------------------
# Function : Send_mail
# Description: Sends email using Gmail SMTP server
# --------------------------------------------------
def Send_mail(destination_path, ReceiverEmail, Scanning_StartTime, Scanning_CompletionTime, NameOfDirectoryScanned, TotalNumberOfFilesScanned, TotalNumberOfDuplicateFilesFound, TotalDeleted):

    body = f"""Jay Ganesh,

            The duplicate-file removal operation has been completed successfully.

            Operation Statistics
            --------------------
            Starting time of directory scanning : {Scanning_StartTime}
            Completion time of directory scanning : {Scanning_CompletionTime}
            Directory scanned                    : {NameOfDirectoryScanned}
            Total number of files scanned        : {TotalNumberOfFilesScanned}
            Total duplicate files found          : {TotalNumberOfDuplicateFilesFound}\n
            Total duplicate files deleted        : {TotalDeleted}

            Please find the detailed log file attached to this email.

            Regards,
            PS Automation System
            """
    
    msg = EmailMessage()

    current_datetime = datetime.datetime.now()
    
    timestamp = current_datetime.strftime("%d_%m_%Y_%H_%M_%S")

    msg["From"] = "testingpythoncode24@gmail.com"
    msg["To"] = ReceiverEmail #"prajakta.shindexam@gmail.com"
    msg["Subject"] = "Regarding duplicate file removal log" + timestamp

    msg.set_content(body)

    # Attach file

    file_path = destination_path

    with open(file_path, "rb") as file:

        file_data = file.read()

        file_name = file.name

    msg.add_attachment(

        file_data,

        maintype="application",

        subtype="octet-stream",

        filename=file_name)

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login("testingpythoncode24@gmail.com", "lcjy ekqd vyxp gszc")
    smtp.send_message(msg)
    smtp.quit()
    print("Email sent successfully.")

def main():
    try:
        if(len(sys.argv) == 2):
            if((sys.argv[1]) == "--h" or (sys.argv[1]) == "--H"):
                print("Duplicate File Removal Automation")
                print("This script scans a directory, identifies duplicate files using checksums, deletes duplicate files, creates a log file, and sends the log file through email.")
                print("Usage:\n python DuplicateFileRemoval.py <DirectoryPath> ‹IntervalInMinutes> <ReceiverEmail> \n Example: python DuplicateFileRemoval.py Test prajakta.shindexam@gmail.com")
                print("For better usages please check --u flag")
            elif((sys.argv[1]) == "--u" or (sys.argv[1]) == "--u"):
                print("The script should support the following Usage option:")
                print("python DuplicateFileRemoval.py --usage or python DuplicateFileRemoval.py -u \nExpected output: Usage: python DuplicateFileRemoval.py <AbsoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>")
            else:
                print("Unable to proceed as arguments are not matching")
                print("Please use --h or --u flag for getting more details")
        elif(len(sys.argv) == 4):
           TimeInterval = int(sys.argv[2])
           if (TimeInterval > 0):
                schedule.every(TimeInterval).minutes.do(DeleteDuplicate, (sys.argv[1]), (sys.argv[3]))
                while True:
                        schedule.run_pending()
                        time.sleep(1)
           else:
                print("Please enter time interval in minutes and above 0 minutes")

    except FileNotFoundError as fObj:
        print("File is not present in the current Directory.")
    except Exception as fObj:
            print("Error occured: ", fObj)

if __name__ == "__main__":
    main()
