text = "Python"
print(id(text))
text = text + "rocks"
print(id(text))

#OUTPUT - Different memory allocation as text data is modified
# 4352329312
# 4352771632