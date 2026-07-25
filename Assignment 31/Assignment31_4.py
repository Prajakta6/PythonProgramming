# Write a program that creates a new log file after every ten minutes.
# The filename should contain the current date and time.
# Example:
# MarvellousLog_25_07_2026_16_30_00.txt
# The file should contain:
# Log file created successfully.
# Creation Time: 25-07-2026 04:30:00 PM

import schedule
import datetime
import time

def CreateLogFile():
    current_datetime = datetime.datetime.now()
    filename = "MarvellousLog_" + current_datetime.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"
    fObj = open(filename, "w")
    fObj.write("Log file created successfully.\n")
    fObj.write("Creation Time: " + current_datetime.strftime("%d-%m-%Y %I:%M:%S %p"))
    print(filename, "created successfully.")
    fObj.close()    
def main():
    print("Automation Script Started")
    schedule.every(10).seconds.do(CreateLogFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

# OUTPUT
# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 31 % python Assignment31_4.py
# Automation Script Started
# MarvellousLog_25_07_2026_13_38_54.txt created successfully.
# MarvellousLog_25_07_2026_13_48_54.txt created successfully.