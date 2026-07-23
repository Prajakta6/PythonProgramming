# Q1) Count Lines in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts how many lines are present in the file.
# Input:
# Demo.txt
# Expected Output:
# Total number of lines in Demo.txt

import os

def Count_File_Lines(filename):
    fObj = open(filename,"r") #RAW code - "r" is read mode
    line_count = 0
    for line in fObj:
        line_count += 1
    return line_count

def main():
    filename = input("Enter the file name: ")
    try:
        line_count = Count_File_Lines(filename)
        print("Total number of lines in", filename, ":", line_count)
    except FileNotFoundError:
        print("File is not present in the current directory.")

if __name__ == "__main__":
    main()

#OUTPUT
# Enter the file name: Demo.txt
# Total number of lines in Demo.txt : 3
