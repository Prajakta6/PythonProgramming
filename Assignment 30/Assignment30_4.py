# Create a task that executes every day at 9:00 AM and prints:
# Namskar...
# Use:
# schedule.every().day.at("09:00").do(...) 

import schedule
import datetime
import time

def Display():
    current_datetime = datetime.datetime.now()
    print("Namskar...", current_datetime.strftime("%d-%m-%Y %I:%M:%S %p"))

def main():
    print("Automation Script Started") 
    schedule.every().day.at("09:00").do(Display)
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

#OUTPUT
# Automation Script Started
# Namskar... 26-07-2026 09:00:00 AM