# Write a Python program using multiprocessing. Pool to calculate the sum of all odd numbers from 1 to N.
# Input
# Data = [1000000, 2000000, 3000000, 4000000]
# Expected Task
# For each number N, calculate:
# 1 + 3 + 5 +...+ N
# Expected Output Format
# Process ID: 1235
# Input Number : 1000000
# Sum of Odd Numbers: 250000000000

import multiprocessing 
import os
import time

def sum_odd(n):
    sum = 0
    for i in range(1, n + 1, 2):
        sum = sum + i

    print("Process ID :", os.getpid())
    print("Input Number :", n)
    print("Sum of Odd Numbers :", sum)
    print()

def main():
    Data = [1000000, 2000000, 3000000, 4000000]
    print("Input string is : ",Data)
    start_time = time.perf_counter()
    pobj = multiprocessing.Pool()
    ret = pobj.map(sum_odd, Data)
    pobj.close()
    pobj.join()
    end_time = time.perf_counter()
    print(f"Time taken is {end_time - start_time: .4f} seconds")

if __name__ == "__main__":
   main()

#OUTPUT
# Input string is :  [1000000, 2000000, 3000000, 4000000]
# Process ID : 5764
# Input Number : 1000000
# Sum of Odd Numbers : 250000000000

# Process ID : 5763
# Input Number : 2000000
# Sum of Odd Numbers : 1000000000000

# Process ID : 5766
# Input Number : 3000000
# Sum of Odd Numbers : 2250000000000

# Process ID : 5770
# Input Number : 4000000
# Sum of Odd Numbers : 4000000000000

# Time taken is  0.1645 seconds