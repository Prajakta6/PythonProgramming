# Write a lambda function using reduce () which accepts a list of numbers and 
# returns the addition of all elements.

from functools import reduce

Addition = lambda No1, No2 :  No1 + No2

def main():
    Data = [10,25,34,56,67]

    print("Input data is : ", Data)

    RData = reduce(Addition, Data)

    print("Data after reduce : ", RData)

if __name__ == "__main__":
    main()

#OUTPUT
# Input data is :  [10, 25, 34, 56, 67]
# Data after reduce :  192