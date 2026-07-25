# Q4) Copy File Contents into Another File
# Problem Statement:
# Write a program which accepts two file names from the user.
# • First file is an existing file
# • Second file is a new file
# Copy all contents from the first file into the second file.
# Input:
# Demo.txt ABC.txt 
# Expected Output:
# Contents of Demo.txt copied into ABC.txt

import sys

def Read_File(filename):
    fObj = open(filename,"r")
    Data = fObj.read()
    print("\nFirst File data : \n")
    print(Data)
    fObj.close() 
    return Data

def Create_File(filename, data):
    fObj = open(filename,"w")
    fObj.write(data)
    fObj = open(filename,"r")
    Data = fObj.read()
    print("\nSecond file data : \n")
    print(Data)
    fObj.close()

def main():
    try:
        firstFileName = input("Enter existing file name : ")
        FirstFileData = Read_File(firstFileName)
        newFileName = input("Enter new file name : ")
        Create_File(newFileName,FirstFileData)
    except FileNotFoundError as fObj:
        print("File is not present in the current Directory.")

if __name__ == "__main__":
    main()

#OUTPUT
# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 28 % python Assignment28_4.py
# Enter existing file name : Demo.txt

# First File data : 

# Jay Ganesh
# Marvellous Infosystems
# Prajakta Shinde
# Enter new file name : ABC2.txt

# Second file data : 

# Jay Ganesh
# Marvellous Infosystems
# Prajakta Shinde
