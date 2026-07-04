# Write a lambda function using filter () which accepts a list of numbers and 
# returns a list of numbers divisible by both 3 and 5.

CheckDivision = lambda no: no % 5 == 0 and no % 3 == 0

def main():
    Data = [1,3,4,5,20,45,9,6,2,9,7]

    print("Input data : ", Data)

    FData = list(filter(CheckDivision, Data))

    print("List of numbers divisible by both 3 and 5: ", FData)

if __name__ == "__main__":
    main()

#OUTPUT
# Input data :  [1, 3, 4, 5, 20, 45, 9, 6, 2, 9, 7]
# List of numbers divisible by both 3 and 5:  [45]

