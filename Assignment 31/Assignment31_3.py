# Write a program that scans a specified directory every minute.
# The task should display:
# • Directory name
# • Number of files
# • Number of subdirectories
# • Date and time of scanning
# Use the os module.
# Example output:
# Directory Scanned: E:/Data
# Total Files: 15
# Total Subdirectories: 4
# Scan Time: 25-07-2026 04:30:00 PM

import os
import schedule
import datetime
import time

def ScanDirectory(path):
    try:
        file_count = 0
        directory_count = 0

        for FolderName, SubFolder, FileName in os.walk(path):
            directory_count += len(SubFolder)
            file_count += len(FileName)

        current_datetime = datetime.datetime.now()

        print("\nDirectory Scanned:", path)
        print("Total Files:", file_count)
        print("Total Subdirectories:", directory_count)
        print("Scan Time:", current_datetime.strftime("%d-%m-%Y %I:%M:%S %p"))

    except Exception as e:
        print("Error:", e)

def main():
    path = "/Users/prajaktashinde/Documents/Marvellous Infosystem /Python Learning/Practicals"
    print("Directory Scanner Started")
    schedule.every(1).minutes.do(ScanDirectory, path)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

# OUTPUT
# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 31 % python Assignment31_3.py
# Directory Scanner Started

# Directory Scanned: /Users/prajaktashinde/Documents/Marvellous Infosystem /Python Learning/Practicals
# Total Files: 231
# Total Subdirectories: 22
# Scan Time: 25-07-2026 01:27:32 PM