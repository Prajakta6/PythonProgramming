# 7. Why does the input () function always return a string?
# How can you convert it to another data type?


# input() always returns a string (str) because keyboard input is read as text.
# Use functions like int(), float(), or bool() to convert the input to the required data type 
# before performing operations on it.

x = input("Enter a number: ")

print(x)
print(type(x))

#OUTPUT
# Enter a number: 10
# 10
# <class 'str'>

x = int(input("Enter a number: "))
print(type(x))

#OUTPUT
# Enter a number: 10
# <class 'int'>

x = float(input("Enter a decimal number: "))
print(type(x))

#OUTPUT
# Enter a decimal number: 10
# <class 'float'>