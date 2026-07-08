# Write a program which contains one lambda function which accepts two parameters 
# and return its multiplication.

mult = lambda no1, no2 : no1 * no2

def main():
    number1 = int(input("Enter number one : "))
    number2 = int(input("Enter number two : "))
    ret = mult(number1, number2)
    print(f"Multiplication of {number1} and {number2} is {ret}")

if __name__ == "__main__":
    main()

#OUTPUT
# Enter number one : 3
# Enter number two : 4
# Multiplication of 3 and 4 is 12