# Q5) Frequency of a String in File
# Problem Statement:
# Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) 
# of that string in the file.
# Input:
# Demo.txt Marvellous
# Expected Output:
# Count how many times "Marvellous" appears in Demo.txt

import sys

def Check_Word_Frequency(fileData, word):
    words = fileData.split()
    count = words.count(word)
    return count

def Read_File(filename):
    fObj = open(filename,"r")
    Data = fObj.read()
    fObj.close() 
    return Data

def main():
    try:
        if(len(sys.argv) == 3):
          FileData = Read_File(sys.argv[1])
          frequencyCount = Check_Word_Frequency(FileData, sys.argv[2])
          print(f"In the file {sys.argv[1]} word {sys.argv[2]} appears {frequencyCount} time/s")
        elif(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
           print("This automation script is used to travel the directory")
           print("For better usages please check --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
           print("Please execute the script as ")
           print("python FileName.py DirectoryName")
           print("DirectoryName should be absolute path")
        else:
         print("Invalid number of argurments")
         print("Please use --h or --u for more information")

    except FileNotFoundError as fObj:
        print("File is not present in the current Directory.")

if __name__ == "__main__":
    main()

#OUTPUT
# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 29 % python Assignment29_5.py Demo.txt Marvellous
# In the file Demo.txt word Marvellous appears 1 time/s