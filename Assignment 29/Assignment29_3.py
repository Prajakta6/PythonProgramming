# Q3) Copy File Contents into a New File (Command Line)
# Problem Statement:
# Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt,
# and copies all contents from the given file into Demo.txt.
# Input (Command Line):
# ABC.txt
# Expected Output:
# Create Demo. txt and copy contents of ABC. txt into Demo. txt.

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
        if(len(sys.argv) == 3):
          FirstFileData = Read_File(sys.argv[1])
          Create_File(sys.argv[2],FirstFileData)
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
# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 29 % python Assignment29_3.py Demo.txt ABC.txt

# First File data : 

# Jay Ganesh
# Marvellous Infosystems
# Prajakta Shinde

# Second file data : 

# Jay Ganesh
# Marvellous Infosystems
# Prajakta Shinde