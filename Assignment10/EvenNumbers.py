# Write a program which accepts one number and prints all even numbers till that number.
# Input: 10
# Output: 2 4 6 8 10

def even_numbers(no):
    evenNumbersList = []
    for i in range(1, no + 1):
        if (i % 2 == 0):
            evenNumbersList.append(i)

    return evenNumbersList

def main():
    number = int(input("Enter a number : "))
    Ret = even_numbers(number)
    print("Even numbers are : ", Ret)

if __name__ == "__main__":
    main()