# 2. Write a program which accepts one number and prints count of digits in that number.
# Input: 7521
# Output: 4

def count_of_digits(no):
    count = len(no)
    return count

def main():
    number = input("Enter a number to count the digits : ")
    Ret = count_of_digits(number)
    print("Count of entered number is : ", Ret)

if __name__ == "__main__":
    main()