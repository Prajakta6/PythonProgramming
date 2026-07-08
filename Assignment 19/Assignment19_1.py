# Write a program which contains one lambda function which accepts one parameter 
# and return power of two.

power_of_two = lambda no: 2 ** no

def main():
    number = int(input("Enter a number : "))
    ret = power_of_two(number)
    print(f"Power of {number} is {ret}")

if __name__ == "__main__":
    main()

#OUTPUT
# Enter a number : 4
# Power of 4 is 16
