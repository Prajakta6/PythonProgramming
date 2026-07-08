def CheckEven(No):
    return (No % 2 == 0)

def main():
    Value = int(input("Enter number : "))

    Ret = CheckEven(Value)

    if(Ret == True):
        print("It's an even number!")
    else:
        print("It's an odd number")

if __name__ == "__main__":
    main()