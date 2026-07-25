# Schedule a task that executes every five minutes.
# The task should write the current date and time into a file named:
# Marvellous.txt
# New entries should be appended without removing previous entries.
# Example file contents:
# Task executed at: 25-07-2026 04:30:00 PM
# Task executed at: 25-07-2026 04:35:00 PM
# Task executed at: 25-07-2026 04:40:00 PM

import schedule
import datetime
import time

def GenerateFileData():
   
    current_datetime = datetime.datetime.now()
    data  = "Task executed at:" + current_datetime.strftime("%d-%m-%Y %I:%M:%S %p") + "\n"
    fObj = open("Marvellous.txt","a")
    fObj.write(data)
    print(data)
    fObj.close()

def main():
    print("Automation Script Started") 
    fObj = open("Marvellous.txt","w")
    schedule.every(5).minutes.do(GenerateFileData)
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

#OUTPUT
# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 30 % python Assignment30_5.py
# Automation Script Started
# Task executed at:25-07-2026 12:14:54 PM
# Task executed at:25-07-2026 12:19:54 PM
# Task executed at:25-07-2026 12:24:54 PM