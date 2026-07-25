# 5: Write a program that deletes all empty files from a specified directory every hour.
# The program should:
# • Scan the directory recursively
# Detect files whose size is zero bytes
# Delete the empty files
# • Store deleted file paths in a log file
# Handle permission errors
# Test the program only on a sample directory.

import os
import schedule
import datetime
import time

def DeleteEmptyFiles(path):
    try:
        if not os.path.isdir(path):
            print("Directory does not exist.")
            return
        
        log = open("DeletedFilesLog.txt", "a")
        log.write("\n")
        log.write("Scan Time : " + datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

        for FolderName, SubFolder, FileName in os.walk(path):
                for file in FileName:
                    filepath = os.path.join(FolderName, file)
                    try:
                        if os.path.getsize(filepath) == 0:
                            os.remove(filepath)
                            print("Deleted:", filepath)
                            log.write(filepath + "\n")
                    except PermissionError:
                        print("Permission denied:", filepath)
                        log.write("Permission denied: " + filepath + "\n")
                    except Exception as e:
                        print("Error:", e)
        log.write("-" * 40 + "\n")
        log.close()
    except Exception as e:
        print("Error:", e)

def main():
    path = input("Enter directory path: ")
    log_file = "deleted_files.log"
    print("Monitoring started... Press Ctrl+C to stop.")
    schedule.every(1).seconds.do(DeleteEmptyFiles, path)
    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
        main()