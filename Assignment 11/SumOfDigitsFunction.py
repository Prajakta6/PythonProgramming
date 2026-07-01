# Write a program which accepts one number and prints sum of digits. 
# Input: 123
# Output: 6

def calculate_sum_of_digits(no):
    sum = 0
    count = len(no)

    for i in range(count):
        sum = sum + int(no[i])

    return sum

def main():
    number = input("Enter a number to calculate it's sum : ")
    
    Ret = calculate_sum_of_digits(number)

    print("Sum of given digit is : ", Ret)


if __name__ == "__main__":
    main()