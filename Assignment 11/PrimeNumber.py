# Write a program which accepts one number and checks whether it is prime or not.
# Input: 11
# Output: Prime Number

def prime_number(no):
    
    if no <= 1:
        print("Not Prime Number")
        return

    for i in range(2, no):
        if no % i == 0:
            print("Not Prime Number")
            return

    print("Prime Number")

def main():
    number = int(input("Enter a number : "))
    prime_number(number)

if __name__ == "__main__":
    main()
