def CheckEven(No):
    return (No % 2 == 0)

def Increament(No):
    return No + 1

def main():
    Data = [13,12,8,10,11,20]
    print("Input data is : ", Data)

    FData = list(filter(CheckEven, Data)) #Check the syntax here, don't add () to CheckEven. 
    #Here we are just giving function name CheckEven and not calling that actual function

    print("Data after filter : ", FData)

    MData = list(map(Increament, FData))

    print("Data after map : ", MData)

if __name__ == "__main__":
    main()
