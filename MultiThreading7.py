import time
import threading

def SumEven(No):
    sum = 0
    for i in range(2,No,2):
        sum = sum + i

    print("Summation of even : ", sum)

def SumOdd(No):
    sum = 0
    for i in range(1,No,2):
        sum = sum +i

    print("Summation of odd : ", sum)

def main():
   
   start_time = time.perf_counter()
   
   t1 = threading.Thread(target=SumEven, args=(100000000,))
   t2 = threading.Thread(target=SumOdd, args=(100000000,))
   
   t1.start()
   t2.start()

   end_time = time.perf_counter()

   print(f"Time required is : {end_time - start_time: .4f} seconds")

if __name__ == "__main__":
    main()

# OUTPUT
# Time required is :  0.0377 seconds
# Summation of odd :  2500000000000000
# Summation of even :  2499999950000000

#Here time is displayed first because it is main theread