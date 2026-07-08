# Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which are even.
# Map function will calculate its square.
# Reduce will return addition of all that numbers.

# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204

from functools import reduce

def check_even_number(no):
    if no % 2 == 0:
        return True
    else:
        return False

def calculate_square(no):
    return no * no

def addition(a, b):
    return a + b

def main():
    data = []
    number_of_elements = int(input("How many elements you want to add? "))

    for i in range(0,number_of_elements):
        number = int(input(f"Enter number: "))
        data.append(number)

    print("Input List = ",data)

    dataf = list(filter(check_even_number,data))
    print(f"List after filter = ",dataf)

    datam = list(map(calculate_square,dataf))
    print(f"List after map = ",datam)
    
    datar = reduce(addition, datam)
    print("Output of reduce =", datar)

if __name__ == "__main__":
    main()

#OUTPUT
# How many elements you want to add? 10
# Enter number: 5
# Enter number: 2
# Enter number: 3
# Enter number: 4
# Enter number: 3
# Enter number: 4
# Enter number: 1
# Enter number: 2
# Enter number: 8
# Enter number: 10
# Input List =  [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter =  [2, 4, 4, 2, 8, 10]
# List after map =  [4, 16, 16, 4, 64, 100]
# Output of reduce = 204