# Write a lambda function using filter () which accepts a list of numbers and 
# returns a list of odd numbers.

OddNumbers = lambda No : No % 2 != 0

def main():

    Data = [1,2,3,4,5,6,7,8,9,10]

    print("Input data is : ", Data)

    FData = list(filter(OddNumbers, Data))

    print("Data after Filter : ", FData)

if __name__ == "__main__":
    main()

#OUTPUT
# Input data is :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Data after Filter :  [1, 3, 5, 7, 9]