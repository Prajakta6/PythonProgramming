# Write a program which accepts one number and prints that many numbers in reverse order.
# Input: 5
# Output: 54321

def reverse_number_series(number):
    numbers = []
    
    for i in range(number, 0, -1):
       numbers.append(i)

    return numbers

def main():
    number = int(input("Enter a number : "))
    Ret = reverse_number_series(number)
    print(Ret)

if __name__ == "__main__":
    main()