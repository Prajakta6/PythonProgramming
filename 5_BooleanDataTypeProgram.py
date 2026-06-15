# 5. Predict the output:
# a = 10
# b = 10
# print(id(a) == id(b))
# Explain why this happens.

a = 10
b = 10
print(id(a) == id(b))

#OUTPUT
#True
#       +------+
# a --->|  10  |
#       +------+
# b -----^

# Why does this happen?

# a and b are assigned the same integer value (10).
# Python interns (caches) small integer objects, typically in the range -5 to 256.
# Instead of creating two separate integer objects with value 10, Python creates one object and lets both variables refer to it.
# THAT'S WHY, a and b point to the same object in memory.