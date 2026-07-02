# Write a lambda function which accepts one number and returns True if divisible by 5.

CheckDivision = lambda no: no % 5 == 0

number = int(input("Enter a number : "))

Ret = CheckDivision(number)

print(Ret)

#OUTPUT
# Enter a number : 4
# False
# Enter a number : 50
# True