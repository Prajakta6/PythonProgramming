def CheckEven(No):
    if (No % 2 == 0 ): # % is mod operator. This condition gives reminder(baki)
        print("It's an even number!")
    else:
        print("It's an odd number")

def main():
    Value = int(input("Enter number : "))

    CheckEven(Value)

if __name__ == "__main__":
    main()