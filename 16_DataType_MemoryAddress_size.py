from sys import getsizeof

x = 10
print(type(x))
print(id(x))
print(getsizeof(x))

x = 10.6
print(type(x))
print(id(x))
print(getsizeof(x))

x = "Jay Ganesh"
print(type(x))
print(id(x))
print(getsizeof(x))


"""
OUTPUT
<class 'int'>
4322586880
28
<class 'float'>
4308436464
24
<class 'str'>
4308603056
51

"""