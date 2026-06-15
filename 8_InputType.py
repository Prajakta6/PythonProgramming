# 8.Predict the output:
# × = input("Enter number: ")
# print(type(x))
# Explain the reason.

#print(type(x)) prints <class 'str'> because input() always returns a string 
# unless it is converted to another data type using functions like int() or float()

x = input("Enter number: ")
print(type(x))

#OUTPUT
# Enter number: 30
# <class 'str'>