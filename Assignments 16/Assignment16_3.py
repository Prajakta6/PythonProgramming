# Write a program which contains one function named as Add() which accepts 
# two numbers from user and return addition of that two numbers.
# Input : 11 5
# Output : 16

import sys

if(len(sys.argv) == 3):

    No1 = int(sys.argv[1])
    No2 = int(sys.argv[2])

    Ans = No1 + No2

    print("Addition is : ",Ans)
else:
    print("Invalid number of arguments!")