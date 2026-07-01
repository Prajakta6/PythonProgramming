# Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.

def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2

def main():
    number1 = int(input("Enter a number1 : "))
    number2 = int(input("Enter a number2 : "))

    addition_result = addition(number1, number2)
    print("Addition of ", number1, "and ", number2, " is : ",addition_result)

    subtraction_result = subtraction(number1, number2)
    print("Subtraction of ", number1, "and ", number2, " is : ",subtraction_result)

    multiplication_result = multiplication(number1, number2)
    print("Multiplication of ", number1, "and ", number2, " is : ",multiplication_result)

    division_result = division(number1, number2)
    print("Division of ", number1, "and ", number2, " is : ",division_result)

if __name__ == "__main__":
    main()

# Enter a number1 : 10
# Enter a number2 : 2
# Addition of  10 and  2  is :  12
# Subtraction of  10 and  2  is :  8
# Multiplication of  10 and  2  is :  20
# Division of  10 and  2  is :  5.0