# Write a lambda function using reduce () which accepts a list of numbers and 
# returns the maximum element.

from functools import reduce

CheckMaximumNumber = lambda No1, No2: No1 if No1 > No2 else No2

def main():
    Data = [10,66,90,22]

    print("Input data : ", Data)

    RData = reduce(CheckMaximumNumber, Data)

    print("Maximum number is : ", RData)

if __name__ == "__main__":
    main()

#OUTPUT
# Enter first number : 3500
# Input data :  [10, 66, 90, 22]
# Maximum number is :  90