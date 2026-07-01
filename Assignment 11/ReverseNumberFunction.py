# Write a program which accepts one number and prints reverse of that number.
# Input: 123
# Output: 321

def reverse_number(no):
    reverse = 0
    while no > 0:
        digit = no % 10 #gets last digit of the number
        reverse = reverse * 10 + digit
        no = no // 10 # divides two numbers and removes the decimal part
    return reverse

def main():
    number = int(input("Enter a number : "))
    ret = reverse_number(number)
    print(ret)

if __name__ == "__main__":
    main()