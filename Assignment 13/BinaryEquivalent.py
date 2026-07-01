# Write a program which accepts one number and prints binary equivalent.

def check_binary_equivalent_number(number):
    return f"{number:08b}"

def main():
    number = int(input("Enetr a number : "))
    ret = check_binary_equivalent_number(number)
    print("Binary Equivalent : ", ret)

if __name__ == "__main__":
    main()

#OUTPUT
# Enetr a number : 2
# Binary Equivalent :  00000010