# Write a lambda function using reduce () which accepts a list of numbers and 
# returns the product of all elements.

from functools import reduce

ProductOfNumbers = lambda No1, No2 : No1 * No2

def main():
    Data = [2,5,6,8,4]

    print("Input data : ", Data)

    RData = reduce(ProductOfNumbers, Data)

    print("Product of numbers is : ", RData)

if __name__ == "__main__":
    main()

#OUTPUT
# Input data :  [2, 5, 6, 8, 4]
# Product of numbers is :  1920