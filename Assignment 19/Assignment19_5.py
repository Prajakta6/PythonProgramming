# Write a program which contains filter()), map() and reduce()) in it. 
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all prime numbers. 
# Map function will multiply each number by 2. 
# Reduce will return Maximum number from that numbers.
# (You can also use normal functions instead of lambda functions).

# Input List = [2, 70, 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62

from functools import reduce

def check_prime_number(no):
    for i in range(2, no):
        if no % i == 0:
            return False

    return True

def multiplication(no):
    return no * 2

def get_maximum(a, b):
    if a > b:
        return a 
    else: 
        return b 

def main():
    data = []
    number_of_elements = int(input("How many elements you want to add? "))

    for i in range(0,number_of_elements):
        number = int(input(f"Enter number: "))
        data.append(number)

    print("Input List = ",data)

    dataf = list(filter(check_prime_number,data))
    print(f"List after filter = ",dataf)

    datam = list(map(multiplication,dataf))
    print(f"List after map = ",datam)
    
    datar = reduce(get_maximum, datam)
    print("Output of reduce =", datar)

if __name__ == "__main__":
    main()

#OUTPUT
# How many elements you want to add? 8
# Enter number: 2
# Enter number: 70
# Enter number: 11
# Enter number: 10
# Enter number: 17
# Enter number: 23
# Enter number: 31
# Enter number: 77
# Input List =  [2, 70, 11, 10, 17, 23, 31, 77]
# List after filter =  [2, 11, 17, 23, 31]
# List after map =  [4, 22, 34, 46, 62]
# Output of reduce = 62