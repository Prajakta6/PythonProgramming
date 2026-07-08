CheckEven = lambda No: (No % 2 == 0) #lambda is keyword

def main():
    Value = int(input("Enter number : "))

    Ret = CheckEven(Value) # Ret = (Value % 2 == 0)

    if(Ret == True):
        print("It's an even number!")
    else:
        print("It's an odd number")

if __name__ == "__main__":
    main()