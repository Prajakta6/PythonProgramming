# Create on module named as Arithmetic which contains 4 functions as Add()
# for addition, Sub()) for subtraction, Mult()) for multiplication and Div()) 
# for division. All functions accepts two parameters as number and perform 
# the operation. Write on python program which call all the functions 
# from Arithmetic module by accepting the parameters from user.

import Arithmetic

def main():
    number1 = int(input("Enter number 1 : "))
    number2 = int(input("Enter number 2 : "))

    addition_result = Arithmetic.Add(number1, number2)
    print(f"Addition of {number1} and {number2} is : ",addition_result)

    subtraction_result = Arithmetic.Sub(number1, number2)
    print(f"Subtraction of {number1} and {number2} is : ",subtraction_result)

    multiplication_result = Arithmetic.Mult(number1, number2)
    print(f"Multiplication of {number1} and {number2} is : ",multiplication_result)

    division_result = Arithmetic.Div(number1, number2)
    print(f"Division of {number1} and {number2} is : ",division_result)

if __name__ == "__main__":
    main()
