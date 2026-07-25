# Write a Python program that monitors the size of a specified file every 30 seconds.
# Write the following details into:
# FileSizelog.txt
# File path
# File size in bytes
# • Date and time
# Handle the situation where the file does not exist.

import os
import schedule
import datetime
import time

def CheckFileSize(filepath):
    current_datetime = datetime.datetime.now()
    fObj = open("FileSizeLog.txt", "a")

    if os.path.exists(filepath):
        filesize = os.path.getsize(filepath)
        fObj.write("File Path : " + filepath + "\n")
        fObj.write("File Size : " + str(filesize) + " bytes\n")
        fObj.write("Date & Time : " + current_datetime.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
        fObj.write("-" * 40 + "\n")
        print("File Size:", filesize, "bytes")
    else:
        fObj.write("File Path : " + filepath + "\n")
        fObj.write("File does not exist.\n")
        fObj.write("Date & Time : " + current_datetime.strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
        fObj.write("-" * 40 + "\n")
        print("File does not exist.")

def main():
    filepath = input("Enter file path: ")
    print("File Monitoring Started")
    schedule.every(30).seconds.do(CheckFileSize, filepath)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

#OUTPUT
# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 32 % python Assignment32_2.py
# Enter file path: /Users/prajaktashinde/Documents/Marvellous Infosystem /Python Learning/Practicals
# File Monitoring Started
# File Size: 160 bytes
# File Size: 160 bytes