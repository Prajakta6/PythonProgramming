# Write a program which accepts one number and checks whether it is perfect number or not.
# Input: 6
# Output: Perfect Number

def check_perfect_number(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum = sum + i

    if sum == number:
        return True
    else:
        return False

def main():
    num = int(input("Enter a number: "))
    ret = check_perfect_number(num)
    if ret == True:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

if __name__ == "__main__":
    main()