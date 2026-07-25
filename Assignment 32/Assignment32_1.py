# Write a program that creates a new text file every minute.
# The filename should contain the current timestamp.
# Example:
# File_25_07_2026_16_30_00.txt
# Write the following information into the file:
# • Filename
# • Creation date
# • Creation time

import schedule
import datetime
import time

def CreateLogFile():
    current_datetime = datetime.datetime.now()
    filename = "File_"+ current_datetime.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"
    fObj = open(filename,"w")
    fObj.write("Filename : " + filename + "\n")
    fObj.write("Creation Date : " + current_datetime.strftime("%d-%m-%Y") + "\n")
    fObj.write("Creation Time : " + current_datetime.strftime("%I:%M:%S %p") + "\n")
    fObj.close()
    print(filename, "created successfully.")

def main():
    print("Automation Script Started")
    schedule.every(1).minutes.do(CreateLogFile)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

#OUTPUT
# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 32 % python Assignment32_1.py
# Automation Script Started
# File_25_07_2026_14_21_21.txt created successfully.
