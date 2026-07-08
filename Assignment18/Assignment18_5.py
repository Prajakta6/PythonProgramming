# Write a program which accept N numbers from user and store it into List.
# Return addition of all prime numbers from that List. 
# Main python file accepts N numbers from user and pass each number to 
# ChkPrime() function which is part of our user defined module named 
# as MarvellousNum. Name of the function from main python file should be ListPrime().
# Input : Number of elements: 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
# Output : 32 (13 + 5 + 7 + 2 + 5)

import MarvellousNum

def ListPrime(Data):
    Sum = 0
    for No in Data:
        if MarvellousNum.ChkPrime(No):
            Sum = Sum + No
    return Sum

def main():
    Size = int(input("Number of elements: "))
    Arr = []
    print("Enter the elements:")
    for i in range(Size):
        Value = int(input())
        Arr.append(Value)
    Result = ListPrime(Arr)
    print("Addition of prime numbers is:", Result)

if __name__ == "__main__":
    main()

#OUTPUT
# Number of elements: 11
# Enter the elements:
# 13
# 5
# 45
# 7
# 4
# 56
# 10
# 34
# 2
# 5
# 8
# Addition of prime numbers is: 32