# Write a Python program that prints:
# Jay Ganesh...
# every two seconds.
# Use:
# schedule.every(2).seconds.do（...）
# Expected output:
# Jay Ganesh...
# Jay Ganesh...
# Jay Ganesh...

import schedule
import datetime
import time

def Display():
    print("Jay Ganesh...", datetime.datetime.now())

def main():
    print("Automation Script Started") 
    schedule.every(2).seconds.do(Display)
    while(True):
        schedule.run_pending() # To check and do remaining work
        time.sleep(1)

if __name__ == "__main__":
    main()

#OUTPUT
# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 30 % python Assignment30_1.py
# Automation Script Started
# Jay Ganesh... 2026-07-25 11:30:41.020330
# Jay Ganesh... 2026-07-25 11:30:43.028931
# Jay Ganesh... 2026-07-25 11:30:45.032661
# Jay Ganesh... 2026-07-25 11:30:47.040548
# Jay Ganesh... 2026-07-25 11:30:49.046162
# Jay Ganesh... 2026-07-25 11:30:51.055671
# Jay Ganesh... 2026-07-25 11:30:53.062801
# Jay Ganesh... 2026-07-25 11:30:55.067880
# Jay Ganesh... 2026-07-25 11:30:57.073478