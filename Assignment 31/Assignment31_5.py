# 5: Write a program that accepts a directory name from the user and counts the number of files inside it 
# every five minutes.
# Write the result into:
# DirectoryCountLog.txt
# Each entry should contain:
# • Directory path
# • Number of files
# • Date and time

import os
import schedule
import datetime
import time

def ScanDirectory(path):
    try:
        file_count = 0

        for FolderName, SubFolder, FileName in os.walk(path):
            file_count += len(FileName)

        current_datetime = datetime.datetime.now()

        print("\nDirectory path : ", path)
        print("Number of files : ", file_count)
        print("Scan Time:", current_datetime.strftime("%d-%m-%Y %I:%M:%S %p"))

        fObj = open("DirectoryCountLog.txt", "a")
        fObj.write("\nDirectory path : " + path + "\n")
        fObj.write("Number of files : " + str(file_count) + "\n")
        fObj.write("Scan Time:" + current_datetime.strftime("%d-%m-%Y %I:%M:%S %p")+ "\n")
        fObj.write("-" * 40 + "\n")
        fObj.close()

    except Exception as e:
        print("Error:", e)

def main():
    path = input("Enter a directory path : ")
    print("Directory Scanner Started")
    schedule.every(5).minutes.do(ScanDirectory, path)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

# OUTPUT
# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 31 % python Assignment31_5.py
# Enter a directory path : /Users/prajaktashinde/Documents/Marvellous Infosystem /Python Learning/Practicals
# Directory Scanner Started

# Directory path :  /Users/prajaktashinde/Documents/Marvellous Infosystem /Python Learning/Practicals
# Number of files :  231
# Scan Time: 25-07-2026 01:50:48 PM