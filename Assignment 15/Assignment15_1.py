# Write a lambda function using map() which accepts a list of numbers and 
# returns a list of squares of each number.

SquareOfNumber = lambda No : No * No

def main():
    Data = [1,2,4,6,8,10]

    print("Input data is : ", Data)

    MData = list(map(SquareOfNumber, Data))

    print("Data after map : ", MData)

if __name__ == "__main__":
    main()

#OUTPUT
# Input data is :  [1, 2, 4, 6, 8, 10]
# Data after map :  [1, 4, 16, 36, 64, 100]