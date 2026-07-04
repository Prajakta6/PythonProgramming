# Write a lambda function using filter () which accepts a list of strings and 
# returns a list of strings having length greater than 5.

CheckLengthOfString = lambda fruit_name: len(fruit_name) > 5

def main():
    Data = ["apple", "banana", "grape", "chikoo"]

    print("Input data : ", Data)

    FData = list(filter(CheckLengthOfString, Data))

    print("List of string which is having length greater than 5: ", FData)

if __name__ == "__main__":
    main()

#OUTPUT
# Input data :  ['apple', 'banana', 'grape', 'chikoo']
# List of string which is having length greater than 5:  ['banana', 'chikoo']