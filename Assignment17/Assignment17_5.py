# Write a program which accept one number for user and check whether number is prime or not.
# Input : 5
# Output : It is Prime Number

def prime_number(no):
    if no <= 1:
        print("Not Prime Number")
        return
    for i in range(2, no):
        if no % i == 0:
            print("Not Prime Number")
            return

    print("It is Prime Number")

def main():
    number = int(input("Enter a number: "))
    prime_number(number)

if __name__ == "__main__":
    main()
