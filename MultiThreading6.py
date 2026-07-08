import time

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
   
   start_time = time.perf_counter()

   SumEven(100000000)
   SumOdd(100000000)

   end_time = time.perf_counter()

   print(f"Time required is : {end_time - start_time: .4f}")

if __name__ == "__main__":
    main()

# OUTPUT
# Summation of even :  2499999950000000
# Summation of odd :  2500000000000000
# Time required is :  2.6835