b = bytes ([65, 66,67])
print (b)

ba = bytearray ([65, 66, 67])
ba[0] = 97
print (ba)

#OUTPUT
# b'ABC' -> ASCII values of integer values
# bytearray(b'aBC') -> As bytearray is mutable after modification updated ASCII values of integer values