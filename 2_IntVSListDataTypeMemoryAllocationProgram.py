# 2. What is the difference between:
# a = 10
# b = 10
# and
# a = [10]
# b = [10]
# Explain using id ()

a = 10
b = 10
print(a)
print(b)
print(id(a))
print(id(b))

a = [10]
b = [10]
print(a)
print(b)
print(id(a))
print(id(b))

#OUTPUT
# 10
# 10
# 4337591072
# 4337591072
# [10]
# [10]
# 4339910976
# 4339912832
#Here Memory allocation for int data type with the same value is same id.
#But in the list data type for same value memory will be differently allocated.
#Also, if you run same program multiple times you will get different memory allocated id every time.