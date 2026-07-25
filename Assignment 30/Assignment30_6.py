# Write a script that schedules the following tasks:
# • Print Lunch Time! every day at 1:00 PM.
# • Print Wrap up work every day at 6:00 PM.
# Both tasks should be handled by separate functions.

import schedule
import datetime
import time

def Display_LunchTime():
    current_datetime = datetime.datetime.now()
    print("Print Lunch Time!", current_datetime.strftime("%d-%m-%Y %I:%M:%S %p"))

def Display_WrapUpWork():
    current_datetime = datetime.datetime.now()
    print("Wrap up work!", current_datetime.strftime("%d-%m-%Y %I:%M:%S %p"))

def main():
    print("Automation Script Started") 
    schedule.every().day.at("13:00").do(Display_LunchTime)
    schedule.every().day.at("18:00").do(Display_WrapUpWork)
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

#OUTPUT
# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 30 % python Assignment30_6.py
# Automation Script Started
# Lunch Time! 25-07-2026 01:00:00 PM
# Wrap up work! 25-07-2026 06:00:00 PM