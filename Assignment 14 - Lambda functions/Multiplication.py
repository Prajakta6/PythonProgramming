# Write a lambda function which accepts two numbers and returns multiplication.

GetMultiplication = lambda no1, no2: no1 * no2

number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))

Ret = GetMultiplication(number1, number2)

print("Multiplication is : ",Ret)

#OUTPUT
# Enter first number : 3
# Enter second number : 4
# Multiplication is :  12