# Write a program which accepts one number and checks whether it is palindrome or not.
# Input: 121
# Output: Palindrome

def check_palindrome(no):
    original = no
    reversed = 0
    while no > 0 :
        digit = no % 10
        reversed = reversed * 10 + digit
        no = no // 10

    if reversed == original:
        print("Palindrome")

def main():
    number = int(input("Enter a number : "))
    check_palindrome(number)


if __name__ == "__main__":
    main()