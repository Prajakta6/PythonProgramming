# Write a lambda function which accepts two numbers and returns maximum number.

CheckMaximumNumber = lambda No1, No2: No1 if No1 > No2 else No2

no1 = int(input("Enter first number : "))
no2 = int(input("Enter first number : "))

max_number = CheckMaximumNumber(no1, no2)

print("Maximum number is : ", max_number)

#OUTPUT
# Enter first number : 3500
# Enter first number : 2300
# Maximum number is :  3500