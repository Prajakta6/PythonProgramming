# Q3) Display File Line by Line
# Problem Statement:
# screen.
# Write a program which accepts a file name from the user and displays the contents of the file line by line on the
# Input: Demo.txt
# Expected Output:
# Display each line of Demo.txt one by one.

def Display_File_Lines(filename):
    fObj = open("Demo.txt","r")
    Data = fObj.read() 
    fObj.close() 
    return Data

def main():
    try:
        filename = input("Enter file name : ")
        file_lines = Display_File_Lines(filename)
        print(f"Lines in {filename} are below : \n {file_lines}")

    except FileNotFoundError as fObj:
        print("File is not present in the current Directory.")

if __name__ == "__main__":
    main()

#OUTPUT
# Enter file name : Demo.txt
# Lines in Demo.txt are below : 
#  Jay Ganesh
# Marvellous Infosystems
# Prajakta Shinde