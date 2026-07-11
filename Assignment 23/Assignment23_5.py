# Write a program that calculates factorials of multiple numbers simultaneously using multiprocessing.Pool.
# Input
# Data = [10, 15, 20, 25]
# Expected Task
# For every N, calculate:
# N!
# Expected Output Format
# Process ID : 1240
# Input Number : 20
# Factorial : 2432902008176640000

import multiprocessing 
import os
import time

def count_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i

    print("Process ID :", os.getpid())
    print("Input Number :", n)
    print("Factorial :", fact)
    print()

def main():
    Data = [10, 15, 20, 25]
    print("Input string is : ",Data)
    start_time = time.perf_counter()
    pobj = multiprocessing.Pool()
    ret = pobj.map(count_factorial, Data)
    pobj.close()
    pobj.join()
    end_time = time.perf_counter()
    print(f"Time taken is {end_time - start_time: .4f} seconds")

if __name__ == "__main__":
   main()

#OUTPUT
# Input string is :  [10, 15, 20, 25]
# Process ID : 6198
# Input Number : 10
# Factorial : 3628800

# Process ID : 6198
# Input Number : 15
# Factorial : 1307674368000

# Process ID : 6198
# Input Number : 20
# Factorial : 2432902008176640000

# Process ID : 6198
# Input Number : 25
# Factorial : 15511210043330985984000000

# Time taken is  0.1195 seconds