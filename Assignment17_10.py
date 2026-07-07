# Write a program which accept number from user and return addition of digits in that number.
# Input 5187934
# Output 37

def calculate_addition_number(No):
    original_no = No
    sum = 0
    while No > 0:
        digit = No % 10
        sum = sum + digit
        No = No // 10
    print(f"Addition of digits in {original_no} number is {sum}")

def main():
    number = int(input("Enter a number : "))
    calculate_addition_number(number)

if __name__ == "__main__":
    main()