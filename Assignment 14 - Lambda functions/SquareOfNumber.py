# Write a lambda function which accepts one number and returns square of that number.

SquareOfNumber = lambda No: No * No

number = int(input("Enter a number : "))

Ret = SquareOfNumber(number)

print("Square of number", number , "is : ", Ret)

# OUTPUT
# Enter a number : 3
# Square of number 3 is :  9