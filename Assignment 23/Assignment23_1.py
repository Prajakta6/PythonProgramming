# Write a Python program using multiprocessing.Pool to calculate the sum of 
# all even numbers from 1 to N for every number from the given list.
# Input
# Data = [1000000, 2000000, 3000000, 4000000]
# Expected Task
# For each number N, calculate:
# 2 + 4 + 6 +...+ N
# Expected Output Format
# Process ID : 1234
# Input Number : 1000000
# Sum of Even Numbers : 250000500000

import multiprocessing 
import os
import time

def sum_even(n):
    sum = 0
    for i in range(2, n + 1, 2):
        sum = sum + i

    print("Process ID :", os.getpid())
    print("Input Number :", n)
    print("Sum of Even Numbers :", sum)
    print()

def main():
    Data = [1000000, 2000000, 3000000, 4000000]
    print("Input string is : ",Data)
    start_time = time.perf_counter()
    pobj = multiprocessing.Pool()
    ret = pobj.map(sum_even, Data)
    pobj.close()
    pobj.join()
    end_time = time.perf_counter()
    print(f"Time taken is {end_time - start_time: .4f} seconds")

if __name__ == "__main__":
   main()

#OUTPUT
# Input string is :  [1000000, 2000000, 3000000, 4000000]
# Process ID : 5625
# Input Number : 1000000
# Sum of Even Numbers : 250000500000

# Process ID : 5629
# Input Number : 2000000
# Sum of Even Numbers : 1000001000000

# Process ID : 5622
# Input Number : 3000000
# Sum of Even Numbers : 2250001500000

# Process ID : 5627
# Input Number : 4000000
# Sum of Even Numbers : 4000002000000

# Time taken is  0.1622 seconds
