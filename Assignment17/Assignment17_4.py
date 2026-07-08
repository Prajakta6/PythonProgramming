# Write a program which accept one number from user and return addition of its factors.
# Input : 12
# Output : 16
# (1+2+3+4+6)

def addition_of_factors(no):
    sum = 0
    for i in range(1, no):
        if no % i == 0:
            sum = sum + i
    return sum

def main():
    number = int(input("Enter a number: "))
    result = addition_of_factors(number)
    print("Addition of factors is:", result)

if __name__ == "__main__":
    main()
