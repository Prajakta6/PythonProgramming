# 4. What is the purpose of getsizeof ()?
# Why is memory size different for different data types?

# sys.getsizeof() returns the memory occupied by an object in bytes.
# Different data types have different memory requirements because of their internal structure and the amount of information they store.
# Complex data types such as lists and dictionaries generally consume more memory than simple data types like integers.

import sys

a = 10
b = 10.5
c = "Python"
print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))

#OUTPUT
# 28
# 24
# 47