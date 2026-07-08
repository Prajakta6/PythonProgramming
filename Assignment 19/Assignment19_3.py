# Write a program which contains filter()), map() and reduce() in it. 
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which greater than or equal to 70 
# and less than or equal to 90. 
# Map function will increase each number by 10. 
# Reduce will return product of all that numbers.

# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000

from functools import reduce

def check_greater_number(no):
    return no >= 70 and no <= 90

def map_numbers(no):
    return no + 10

def multiply(a, b):
    return a * b

def main():
    data = []
    number_of_elements = int(input("How many elements you want to add? "))

    for i in range(0,number_of_elements):
        number = int(input(f"Enter number: "))
        data.append(number)

    print("Input List = ",data)

    dataf = list(filter(check_greater_number,data))
    print(f"List after filter = ",dataf)

    datam = list(map(map_numbers,dataf))
    print(f"List after map = ",datam)
    
    datar = reduce(multiply, datam)
    print("Output of reduce =", datar)

if __name__ == "__main__":
    main()

#OUTPUT
# How many elements you want to add? 12
# Enter number: 4
# Enter number: 34
# Enter number: 36
# Enter number: 76
# Enter number: 68
# Enter number: 24
# Enter number: 89
# Enter number: 23
# Enter number: 86
# Enter number: 90
# Enter number: 45
# Enter number: 70
# Input List =  [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter =  [76, 89, 86, 90, 70]
# List after map =  [86, 99, 96, 100, 80]
# Output of reduce = 6538752000