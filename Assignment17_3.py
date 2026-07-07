# Write a program which accept one number from user and return its factorial.
# Input : 5
# Output : 120

def factorial(No):
    fact = 1
    for i in range(1, No + 1):
        fact = fact * i

    print(fact)

def main():
    number = int(input("Enter a number : "))
    factorial(number)

if __name__ == "__main__":
    main()