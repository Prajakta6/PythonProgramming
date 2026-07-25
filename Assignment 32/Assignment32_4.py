# Write a program that copies all .txt files from one directory to another every ten minutes.
# The program should:
# • Accept source and destination directories
# • Validate both directories
# • Copy only .txt files
# • Maintain a log of copied files
# • Avoid terminating if one file cannot be copied

import os
import shutil
import schedule
import datetime
import time

def CopyTextFiles(source, destination):
    if not os.path.isdir(source):
        print("Source directory does not exist.")
        return
    
    if not os.path.isdir(destination):
        print("Destination directory does not exist.")
        return

    log = open("CopyLog.txt", "a")
    log.write("\n")
    log.write("Copy Operation: " + datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

    for filename in os.listdir(source):
        source_file = os.path.join(source, filename)
        if os.path.isfile(source_file) and filename.endswith(".txt"):
            destination_file = os.path.join(destination, filename)
            try:
                shutil.copy2(source_file, destination_file)
                print(filename, "copied successfully.")
                log.write(filename + " : Copied Successfully\n")
            except Exception as e:
                print("Error copying", filename)
                log.write(filename + " : Failed - " + str(e) + "\n")
    log.write("-" * 40 + "\n")

def main():
    source = input("Enter source directory: ")
    destination = input("Enter destination directory: ")
    print("Automation Script Started")
    schedule.every(10).minutes.do(CopyTextFiles, source, destination)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
    
#OUTPUT
# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 32 % python Assignment32_4.py
# Enter source directory: /Users/prajaktashinde/Documents/Marvellous Infosystem /SourceFiles            
# Enter destination directory: /Users/prajaktashinde/Documents/Marvellous Infosystem /DestinationFiles
# Automation Script Started
# CopyLog.txt copied successfully.
# ABC2.txt copied successfully.
# CopyLog.txt copied successfully.
# ABC2.txt copied successfully.
# CopyLog.txt copied successfully.
# ABC2.txt copied successfully.
# CopyLog.txt copied successfully.
# ABC2.txt copied successfully.