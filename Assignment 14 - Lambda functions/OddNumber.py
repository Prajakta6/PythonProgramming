# Write a lambda function which accepts one number and returns True if number is odd otherwise False.

CheckOddNumber = lambda no: no % 2 != 0

number = int(input("Enter a number :"))

Ret = CheckOddNumber(number)

print(Ret)

#OUTPUT
# Enter a number :2
# False
# Enter a number :5
# True