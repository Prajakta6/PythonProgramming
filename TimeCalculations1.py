#6! = 1 * 2 * 3 * 4 * 5 * 6

def factorial(no):
    Fact = 1

    for i in range(1,no+1): 
        Fact = Fact * i 

    return Fact

def main():
    
    value = int(input("Enter a number :"))

    Ret = factorial(value)

    print("Factorial of " ,value, " is : ", Ret)

if __name__ == "__main__":
    main()

# #OUTPUT
# Enter a number :6
# Factorial of  6  is :  720

# Enter a number :20
# Factorial of  20  is :  2432902008176640000
