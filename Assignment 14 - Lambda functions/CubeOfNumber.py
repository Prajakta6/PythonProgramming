# Write a lambda function which accepts one number and returns cube of that number.

CubeOfNumber = lambda no: no * no * no

number = int(input("Enter a number : "))

Ret = CubeOfNumber(number)

print("Cube of number", number , "is : ", Ret)

# OUTPUT
# Enter a number : 3
# Cube of number 3 is :  27