#Write a lambda function which accepts one number and returns True if number is even otherwise False.

CheckEven = lambda No : No % 2 == 0 

number = int(input("Enter a number :"))

Ret = CheckEven(number)

print(Ret)

#OUTPUT
# Enter a number :2
# True
# Enter a number :5
# False