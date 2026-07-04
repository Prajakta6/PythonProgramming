# Write a lambda function using filter () which accepts a list of numbers and 
# returns a list of even numbers.

EvenNumber = lambda No : No % 2 == 0

def main():
    Data = [1,2,5,6,8,11]

    print("Input data is : ", Data)

    FData = list(filter(EvenNumber, Data))

    print("Data after Filter : ", FData)

if __name__ == "__main__":
    main()

# OUTPUT
# Input data is :  [1, 2, 5, 6, 8, 11]
# Data after Filter :  [2, 6, 8]