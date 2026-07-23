# Q5) Search a Word in File
# Problem Statement:
# Write a program which accepts a file name and a word from the user and checks whether that word is present
# in the file or not.
# Input:
# Demo.txt Marvellous
# Expected Output:
# Display whether the word Marvellous is found in Demo. txt or not.

import sys

def Is_Word_Present(filename, wordToSearch):
    fObj = open(filename,"r")
    Data = fObj.read()
    IsWordPresent = ""
    if wordToSearch in Data:
       IsWordPresent = "found in " + filename
    else:
       IsWordPresent = "not found in " + filename
    fObj.close() 
    return IsWordPresent

def main():
    try:
        if(len(sys.argv) == 3):
          IsWordPresent = Is_Word_Present(sys.argv[1], sys.argv[2])
          print(f"The word {sys.argv[2]} is {IsWordPresent}")
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
# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 28 % python Assignment28_5.py Demo.txt Marvellous
# The word Marvellous is found in Demo.txt

# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 28 % python Assignment28_5.py Demo.txt Marvellouss
# The word Marvellouss is not found in Demo.txt