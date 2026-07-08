import threading #module name

# 2+4+6+8 = 20
def SumEven(No):
    sum = 0
    for i in range(2,No,2):
        sum = sum + i

    print("Summation of even : ", sum)

# 1+3+5+7+9 = 25
def SumOdd(No):
    sum = 0
    for i in range(1,No,2):
        sum = sum +i

    print("Summation of odd : ", sum)

def main():
   SumEven(10000000000)
   SumOdd(10000000000)

if __name__ == "__main__":
    main()

# OUTPUT
# Summation of even :  20
# Summation of odd :  25