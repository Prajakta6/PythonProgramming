import os
import time
import multiprocessing

def SumEven(No):
    print(f"PID of SumEven : {os.getpid()} PPID of SumEven : {os.getppid()}")
    sum = 0
    for i in range(2,No,2):
        sum = sum + i

    print("Summation of even : ", sum)

def SumOdd(No):
    print(f"PID of SumOdd : {os.getpid()} PPID of SumOdd : {os.getppid()}")
    sum = 0
    for i in range(1,No,2):
        sum = sum +i

    print("Summation of odd : ", sum)

def main():
   print(f"PID of Main : {os.getpid()} PPID of Main : {os.getppid()}")
   start_time = time.perf_counter() #
   
   t1 = multiprocessing.Process(target=SumEven, args=(100,))
   t2 = multiprocessing.Process(target=SumOdd, args=(100,))
   
   t1.start()
   t2.start()
   
   t1.join()
   t2.join()

   end_time = time.perf_counter()

   print(f"Time required is : {end_time - start_time: .4f} seconds")

if __name__ == "__main__":
    main()

# OUTPUT
# PID of Main : 2124 PPID of Main : 1197
# PID of SumEven : 2126 PPID of SumEven : 2124
# Summation of even :  2450
# PID of SumOdd : 2127 PPID of SumOdd : 2124
# Summation of odd :  2500
# Time required is :  0.0472 seconds

#Note : 
# PPID - 1197  => Command prompt id
# PPID - 2124  => MainThread id
# PPID - 2126  => SumEven id
# PPID - 2127  => SumOdd id