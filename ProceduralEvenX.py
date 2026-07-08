def CheckEven(No):
    if (No % 2 == 0 ): # % is mod operator. This condition gives reminder(baki)
        return True
    else:
        return False

def main():
    Value = int(input("Enter number : "))

    Ret = CheckEven(Value)

    if(Ret == True):
        print("It's an even number!")
    else:
        print("It's an odd number")

if __name__ == "__main__":
    main()