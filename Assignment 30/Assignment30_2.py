# Write a Python program that displays the current date and time after every one minute.
# Use the datetime module.
# Expected output:
# Current Date and Time: 25-07-2026 04:30:00 PM

import schedule
import datetime
import time

def Display():
    current_datetime = datetime.datetime.now()
    print("Current Date and Time:", current_datetime.strftime("%d-%m-%Y %I:%M:%S %p"))

def main():
    print("Automation Script Started") 
    schedule.every(1).minutes.do(Display)
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

#OUTPUT
# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 30 % python Assignment30_2.py
# Automation Script Started
# Current Date and Time: 25-07-2026 11:37:42 AM
# Current Date and Time: 25-07-2026 11:38:42 AM