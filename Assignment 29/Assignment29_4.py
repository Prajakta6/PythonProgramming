# Q4) Compare Two Files (Command Line)
# Problem Statement:
# Write a program which accepts two file names through command line arguments and compares the contents of both files.
# • If both files contain the same contents, display Success
# • Otherwise display Failure
# Input (Command Line):
# Demo.txt Hello.txt
# Expected Output:
# Success OR Failure

import sys

def CompareFiles(file1Data, file2Data):
    if file1Data == file2Data:
        print("Success")
    else:
        print("Failure")

def Read_File(filename):
    fObj = open(filename,"r")
    Data = fObj.read()
    fObj.close() 
    return Data

def main():
    try:
        if(len(sys.argv) == 3):
          FirstFileData = Read_File(sys.argv[1])
          SecondFileData = Read_File(sys.argv[2])
          CompareFiles(FirstFileData,SecondFileData)
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
# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 29 % python Assignment29_4.py Demo.txt ABC.txt
# Success

# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 29 % python Assignment29_4.py Demo.txt Hello.txt
# Failure