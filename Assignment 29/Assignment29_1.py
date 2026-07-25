# Q1) Check File Exists in Current Directory
# Problem Statement:
# Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.
# Input:
# Demo.txt
# Expected Output:
# Display whether Demo.txt exists or not.

import sys
import os

def Check_File_Exists(filename, directory):
    found = False

    print("\n Current Directory:", os.getcwd()+"\n")
    
    print("Searching Directory:", os.path.abspath(directory)+"\n")

    for FolderName, SubFolderName, FileName in os.walk(directory):
        for fName in FileName:
            if fName == filename:
                found = True
                break
        if found:
            break
    if found:
        print(f"{filename} exists")
    else:
        print(f"{filename} does not exist")

def main():
    if(len(sys.argv) == 3):
       Check_File_Exists(sys.argv[1], sys.argv[2])
    elif(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
        print("For better usages please check --u flag")
    elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
        print("Please execute the script as ")
        print("python FileName.py DirectoryName")
        print("DirectoryName should be absolute path")
    else:
       print("Invalid number of argurments")
       print("Please use --h or --u for more information")

if __name__ == "__main__":
    main()

#OUTPUT
# ********************************* CORRECT FILE SEARCH BELOW ********************************* 

# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 29 % python Assignment29_1.py Demo.txt .

#  Current Directory: /Users/prajaktashinde/Documents/Marvellous Infosystem /Python Learning/My Assignments/Assignment 29

# Searching Directory: /Users/prajaktashinde/Documents/Marvellous Infosystem /Python Learning/My Assignments/Assignment 29

# Demo.txt exists

# ********************************* ERROR BELOW ********************************* 

# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 29 % python Assignment29_1.py Demo.txt "Assignment 29"

#  Current Directory: /Users/prajaktashinde/Documents/Marvellous Infosystem /Python Learning/My Assignments/Assignment 29

# Searching Directory: /Users/prajaktashinde/Documents/Marvellous Infosystem /Python Learning/My Assignments/Assignment 29/Assignment 29

# Demo.txt does not exist
