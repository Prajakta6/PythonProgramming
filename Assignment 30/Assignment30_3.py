# Write a program that schedules a function to print:
# Coding Kar..! every 30 minutes.

import schedule
import datetime
import time

def Display():
    current_datetime = datetime.datetime.now()
    print("Coding Kar..!", current_datetime.strftime("%d-%m-%Y %I:%M:%S %p"))

def main():
    print("Automation Script Started") 
    schedule.every(30).minutes.do(Display)
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

#OUTPUT
# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 30 % python Assignment30_3.py
# Automation Script Started
# Coding Kar..! 25-07-2026 11:40:56 AM
# Coding Kar..! 25-07-2026 12:10:56 AM