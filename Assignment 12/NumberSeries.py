# Write a program which accepts one number and prints that many numbers starting from 1.
# Input: 5
# Output: 1 2 3 4 5

def number_series(number):
    numbers = []
    
    for i in range(1, number + 1):
        numbers.append(i)

    return numbers

def main():
    number = int(input("Enter a number : "))
    Ret = number_series(number)
    print(Ret)

if __name__ == "__main__":
    main()