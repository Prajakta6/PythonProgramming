# Write a lambda function which accepts three numbers and returns largest number.
#FindLargeNumber.py

FindLargeNumber = lambda no1, no2, no3: no1 if no1 >= no2 and no1 >= no3 else (no2 if no2 >= no3 else no3)

number1 = int(input("Enter first number : "))
number2 = int(input("Enter second number : "))
number3 = int(input("Enter third number : "))

Ret = FindLargeNumber(number1, number2, number3)

print("Large number is : ",Ret)

#OUTPUT
# Enter first number : 34
# Enter second number : 67
# Enter third number : 23
# Large number is :  67
#**************************************************
# Enter first number : 105
# Enter second number : 34
# Enter third number : 90
# Large number is :  105