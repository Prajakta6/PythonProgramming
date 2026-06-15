# What does the id () function return?
# Is the value returned by id () same for two variables holding the same value?

#The id() function returns the unique identity (memory allocated address) of an object during its lifetime.
#Not always. It depends on whether the two variables refer to the same object.
x = 100
y = 100
print(x)
print(y)
print(id(x))
print(id(y))

x = [100]
y = [100]
print(x)
print(y)
print(id(x))
print(id(y))

#OUTPUT
# 100
# 100
# 4380159584
# 4380159584
# [100]
# [100]
# 4382476608
# 4382478464