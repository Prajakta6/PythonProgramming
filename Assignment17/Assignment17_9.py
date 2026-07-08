# Write a program which accept number from user and return number of digits in that number.
# Input 5187934
# Output 7

def calculate_length_number(No):
    print(f"Number of digits in {No} number is {len(No)}")

def main():
    number = input("Enter a number : ")
    calculate_length_number(number)

if __name__ == "__main__":
    main()
