# Create a function named:
# DisplayMessage (message)
# Schedule the function using:
# schedule.every (5). seconds. do (Displaymessage, message)
# The message should be accepted from the user.

import schedule
import datetime
import time

def DisplayMessage(message):
    current_datetime = datetime.datetime.now()
    print(message, current_datetime.strftime("%d-%m-%Y %I:%M:%S %p"))

def main():
    message = input("Enter a message : ")
    schedule.every(5).seconds.do(DisplayMessage, message)
    while(True):
        schedule.run_pending()
        time.sleep(1)
if __name__ == "__main__":
    main()

#OUTPUT
# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 31 % python Assignment31_2.py
# Enter a message : Jay Ganesh
# Jay Ganesh 25-07-2026 01:06:08 PM
# Jay Ganesh 25-07-2026 01:06:13 PM
# Jay Ganesh 25-07-2026 01:06:18 PM