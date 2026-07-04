# Write a lambda function using filter () which accepts a list of numbers and 
# returns the count of even numbers.

CheckEven = lambda No : (No % 2 == 0)

def filterX(Task, Elements):
    Result = []

    for no in Elements:
        Ret = Task(no) #CheckEven(no)
        if(Ret == True):
            Result.append(no)

    return Result

def main():
    Data = [13,12,8,10,11,20]

    print("Input data is : ", Data)

    FData = list(filterX(CheckEven, Data)) 

    print("Data after filter : ", FData)

    print("Count of even numbers: ",len(FData))

if __name__ == "__main__":
    main()

# OUTPUT
# Input data is :  [13, 12, 8, 10, 11, 20]
# Data after filter :  [12, 8, 10, 20]
# Count of even numbers:  4
