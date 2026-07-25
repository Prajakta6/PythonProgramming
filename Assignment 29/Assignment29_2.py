# Q2) Display File Contents
# Problem Statement:
# console.
# Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the
# Input:
# Demo.txt
# Expected Output:
# Display contents of Demo.txt on console.

def main():
    try:
        fileName = input("Enter file name : ")
        fObj = open(fileName,"r") #RAW code - "r" is read mode
        print("File gets opened")
        Data = fObj.read() #Reading the data from the file
        print(Data)
        fObj.close() #close the file after it's use gets completed

    except FileNotFoundError as fObj:
        print("File is not present in the current Directory.")

if __name__ == "__main__":
    main()

#OUTPUT
# (base) prajaktashinde@Prajaktas-MacBook-Pro Assignment 29 % python Assignment29_2.py
# Enter file name : Demo.txt
# File gets opened
# Jay Ganesh
# Marvellous Infosystems
# Prajakta Shinde