# Write a program that counts how many even numbers exist between 1 and N using Pool.map().
# Input
# Data = [1000000, 2000000, 3000000, 4000000]
# Expected Output Format
# Process ID : 1236
# Input Number : 1000000
# Even Number Count : 500000

import multiprocessing 
import os
import time

def count_even(n):
    count = 0
    for i in range(2, n + 1, 2):
        count = count + 1

    print("Process ID :", os.getpid())
    print("Input Number :", n)
    print("Count of Even Numbers :", count)
    print()

def main():
    Data = [1000000, 2000000, 3000000, 4000000]
    print("Input string is : ",Data)
    start_time = time.perf_counter()
    pobj = multiprocessing.Pool()
    ret = pobj.map(count_even, Data)
    pobj.close()
    pobj.join()
    end_time = time.perf_counter()
    print(f"Time taken is {end_time - start_time: .4f} seconds")

if __name__ == "__main__":
   main()

#OUTPUT
# Input string is :  [1000000, 2000000, 3000000, 4000000]
# Process ID : 5932
# Input Number : 1000000
# Count of Even Numbers : 500000

# Process ID : 5931
# Input Number : 2000000
# Count of Even Numbers : 1000000

# Process ID : 5934
# Input Number : 3000000
# Count of Even Numbers : 1500000

# Process ID : 5930
# Input Number : 4000000
# Count of Even Numbers : 2000000

# Time taken is  0.1597 seconds