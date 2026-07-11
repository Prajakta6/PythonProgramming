# Write a program that calculates
# 1^5+2^5+3^5+.....+N^5
# for multiple values of N simultaneously using Pool.
# Input
# [1000000,
# 2000000,
# 3000000,
# 4000000]
# Measure total execution time.

import multiprocessing
import time

def calculate_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + (i ** 5) # i^5
    return sum

def main():

    data = [1000000,2000000,3000000,4000000]
    print("Input list is : ",data)
    start_time = time.perf_counter()
    pobj = multiprocessing.Pool()
    Result = pobj.map(calculate_sum,data)
    pobj.close()
    pobj.join()
    end_time = time.perf_counter()
    print("Result is : ", Result)
    print(f"Total execution time is {end_time - start_time : .4f} seconds")

if __name__ == "__main__":
    main()

#OUTPUT
# Input list is :  [1000000, 2000000, 3000000, 4000000]
# Result is :  [166667166667083333333333250000000000, 10666682666673333333333333000000000000, 121500121500033749999999999250000000000, 682667178666773333333333332000000000000]
# Total execution time is  0.5011 seconds