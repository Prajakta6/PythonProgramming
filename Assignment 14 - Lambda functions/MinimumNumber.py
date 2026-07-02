# Write a lambda function which accepts two numbers and returns minimum number.

CheckMinimumNumber = lambda No1, No2: No1 if No1 < No2 else No2

no1 = int(input("Enter first number : "))
no2 = int(input("Enter first number : "))

min_number = CheckMinimumNumber(no1, no2)

print("Minimum number is : ", min_number)

#OUTPUT
# Enter first number : 50
# Enter first number : 100
# Minimum number is :  50