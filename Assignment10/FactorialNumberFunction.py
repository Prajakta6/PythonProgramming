# Write a program which accepts one number and prints factorial of that number.
# Input: 5
# Output: 120

def factorial_number(no):
    factNumber = 1
    for i in range(1, no + 1):
        factNumber = factNumber * i
    return factNumber

def main():
    number = int(input("Enter a number : "))
    Ret = factorial_number(number)
    print("Factorial of",number," is ", Ret)

if __name__ == "__main__":
    main()