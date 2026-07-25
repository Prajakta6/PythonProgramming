# Write a program that accepts:
# • A message from the user
# • A time interval in seconds
# Schedule the program to display the message repeatedly after the specified interval.
# Example input:
# Enter message: Jay Ganesh
# Enter interval in seconds: 5
# Expected output:
# Jay Ganesh
# every five seconds.
# Validate that the interval is greater than zero.

import schedule
import datetime
import time

def Display_Message(message):
    current_datetime = datetime.datetime.now()
    print(message, current_datetime.strftime("%d-%m-%Y %I:%M:%S %p"))

def main():
    message = input("Enter a message : ")
    interval = int(input("Enter interval in seconds: "))
    if interval > 0:
        schedule.every(interval).seconds.do(Display_Message, message)
        while(True):
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Please enter a valid interval in seconds")
if __name__ == "__main__":
    main()

#OUTPUT
# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 31 % python Assignment31_1.py
# Enter a message : Jay Ganesh...
# Enter interval in seconds: 5
# Jay Ganesh... 25-07-2026 12:47:57 PM
# Jay Ganesh... 25-07-2026 12:48:02 PM

# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 31 % python Assignment31_1.py
# Enter a message : Jay Ganesh...
# Enter interval in seconds: 0
# Please enter a valid interval in seconds
