# Write a lambda function using reduce () which accepts a list of numbers and 
# returns the minimum element.

from functools import reduce

CheckMinimumNumber = lambda No1, No2: No1 if No1 < No2 else No2

def main():
    Data = [10,66,90,22]

    print("Input data : ", Data)

    RData = reduce(CheckMinimumNumber, Data)

    print("Minimum number is : ", RData)

if __name__ == "__main__":
    main()

#OUTPUT
# Enter first number : 3500
# Input data :  [10, 66, 90, 22]
# Minimum number is :  10