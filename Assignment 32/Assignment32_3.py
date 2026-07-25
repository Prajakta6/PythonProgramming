# Write a program that reads and displays the contents of a specified text file every minute.
# Handle the following conditions:
# • File does not exist
# • File is empty
# • Permission is denied
# • File cannot be opened

import schedule
import time
import os

def ReadFile(filename):
    try:
        fObj = open(filename, "r")
        data = fObj.read()

        if len(data) == 0:
            print("File is empty.")
        else:
            print("\nFile Contents:")
            print(data)

    except FileNotFoundError:
        print("File does not exist.")

    except PermissionError:
        print("Permission denied.")

    except OSError:
        print("File cannot be opened.")

def main():
    filename = input("Enter file name: ")
    print("File Reader Started")
    schedule.every(1).minutes.do(ReadFile, filename)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

#OUTPUT
# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 32 % python Assignment32_3.py
# Enter file name: FileSizeLog.txt
# File Reader Started

# File Contents:
# File Path : /Users/prajaktashinde/Documents/Marvellous Infosystem /Python Learning/Practicals
# File Size : 160 bytes
# Date & Time : 25-07-2026 02:26:42 PM
# ----------------------------------------
# File Path : /Users/prajaktashinde/Documents/Marvellous Infosystem /Python Learning/Practicals
# File Size : 160 bytes
# Date & Time : 25-07-2026 02:27:12 PM
# ----------------------------------------
# File Path : /Users/prajaktashinde/Documents/Marvellous Infosystem /Python Learning/Practicals
# File Size : 160 bytes
# Date & Time : 25-07-2026 02:27:42 PM
# ----------------------------------------
# File Path : /Users/prajaktashinde/Documents/Marvellous Infosystem /Python Learning/Practicals
# File Size : 160 bytes
# Date & Time : 25-07-2026 02:28:13 PM
# ----------------------------------------
# File Path : /Users/prajaktashinde/Documents/Marvellous Infosystem /Python Learning/Practicals
# File Size : 160 bytes
# Date & Time : 25-07-2026 02:28:43 PM
# ----------------------------------------
# File Path : /Users/prajaktashinde/Documents/Marvellous Infosystem /Python Learning/Practicals
# File Size : 160 bytes
# Date & Time : 25-07-2026 02:29:13 PM
# ----------------------------------------