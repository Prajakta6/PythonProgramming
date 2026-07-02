# Write a lambda function which accepts two numbers and returns addition.

GetAddition = lambda no1, no2: no1 + no2

number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))

Ret = GetAddition(number1, number2)

print("Addition is : ",Ret)

#OUTPUT
# Enter first number : 5
# Enter second number : 15
# Addition is :  20