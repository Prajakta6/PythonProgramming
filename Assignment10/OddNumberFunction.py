# Write a program which accepts one number and prints
# all odd numbers till that number.

def odd_numbers(no):
    oddNumbersList = []
    for i in range(1, no + 1):
        if (i % 2 != 0):
            oddNumbersList.append(i)

    return oddNumbersList

def main():
    number = int(input("Enter a number : "))
    Ret = odd_numbers(number)
    print("Odd numbers are : ", Ret)

if __name__ == "__main__":
    main()