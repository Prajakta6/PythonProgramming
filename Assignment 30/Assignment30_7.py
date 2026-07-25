# Write a Python program that performs a file backup every hour.
# The program should:
# Accept the source file path.
# 2. Accept the destination directory path.
# 3. Copy the source file to the destination directory.
# 4. Add the current date and time to the backup filename.
# 5. Write the backup operation details into:
# backup_log.txt
# Example backup filename:
# Data_25_07_2026_16_30_00.txt
# Example log entry:
# Backup completed successfully at 25-07-2026 04:30:00 PM
# Use the shutil module for file copying.

import schedule
import shutil
import os
import datetime
import time

def BackupFile(source_file, destination_dir):
    try:
        print("Source File:", source_file)
        print("Destination Directory:", destination_dir)
        current_datetime = datetime.datetime.now()
        filename = os.path.basename(source_file)
        name, ext = os.path.splitext(filename)

        timestamp = current_datetime.strftime("%d_%m_%Y_%H_%M_%S")
        backup_filename = f"{name}_{timestamp}{ext}"

        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        destination_path = os.path.join(destination_dir, backup_filename)

        shutil.copy2(source_file, destination_path)

        log_message = "Backup completed successfully at " + current_datetime.strftime("%d-%m-%Y %I:%M:%S %p") + "\n"

        with open("backup_log.txt", "a") as log_file:
            log_file.write(log_message)

        print(log_message)

    except Exception as e:
        print("Error:", e)


def main():
    source_file = input("Enter source file path: ")
    destination_dir = input("Enter destination directory path: ")
    print("Backup Automation Started")
    schedule.every().hour.do(BackupFile, source_file, destination_dir)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

#OUTPUT
# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 30 % python Assignment30_7.py
# Enter source file path: Marvellous.txt
# Enter destination directory path: Backup
# Backup Automation Started
# Source File: Marvellous.txt
# Destination Directory: Backup
# Backup completed successfully at 25-07-2026 12:30:35 PM

# Source File: Marvellous.txt
# Destination Directory: Backup
# Backup completed successfully at 25-07-2026 13:30:35 PM

# Source File: Marvellous.txt
# Destination Directory: Backup
# Backup completed successfully at 25-07-2026 14:30:35 PM