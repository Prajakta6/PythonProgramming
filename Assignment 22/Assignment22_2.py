# Write a program that calculates factorials of multiple numbers simultaneously using Pool.map().
# Input
# [10,15,20,25]
# Display :
# Process ID
# Input Number
# Factorial

import multiprocessing
import time
import os

def factorial_no(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return (os.getpid(), n, fact)

def main():
    data = [10,15,20,25]

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()
    Result = pobj.map(factorial_no,data) 
    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    for pid, no, fact in Result:

        print("Process ID :", pid)

        print("Input Number :", no)

        print("Factorial :", fact)

        print()

    print("Result is ")
    print(Result)

    print(f"Time take is {end_time - start_time: .4f} seconds")

if __name__ == "__main__":
    main()

#OUTPUT
# Process ID : 8041
# Input Number : 10
# Factorial : 3628800

# Process ID : 8041
# Input Number : 15
# Factorial : 1307674368000

# Process ID : 8041
# Input Number : 20
# Factorial : 2432902008176640000

# Process ID : 8041
# Input Number : 25
# Factorial : 15511210043330985984000000

# Result is 
# [(8041, 10, 3628800), (8041, 15, 1307674368000), (8041, 20, 2432902008176640000), (8041, 25, 15511210043330985984000000)]
# Time take is  0.1135 seconds