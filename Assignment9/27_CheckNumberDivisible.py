# Write a program which accepts one number and checks whether it is divisible by 3 and
# 5
# Input: 15
# Output: Divisible by 3 and 5

def CheckNumberDivisible(No):
    if(No % 3 == 0 and No % 5 == 0):
        print("Divisible by 3 and 5")
    else:
        print("Not divisible!!")

def main():
    number = int(input("Enter number : "))
    CheckNumberDivisible(number)

if __name__ == "__main__":
    main()