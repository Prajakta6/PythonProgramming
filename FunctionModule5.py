from Marvellous import *

def main():
    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    Ret = Addition(Value1, Value2)
    print("Addition is : ", Ret)

    Ret = Substraction(Value1, Value2)
    print("Substraction is : ", Ret)

if __name__ == "__main__":
    main()

# OUTPUT
# Enter first number : 
# 11
# Enter second number : 
# 10
# Addition is :  21
# Substraction is :  1