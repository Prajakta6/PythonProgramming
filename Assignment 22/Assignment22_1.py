# Write a program that accepts a list of integers and uses Pool.map() to calculate 
# the sum of squares from 1 to N for every element in the list.

#Example input
# [1000000, 2000000, 3000000, 4000000]
# Expected Output
# [333333833333500000,
# 2666668666667000000,
# ...
# ]

import multiprocessing
import time

def sum_of_squares(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + (i * i)
    return sum


def main():
    number = int(input("Enter no of elements : "))
    data = []
    for n in range(number):
        no = int(input("Enter no : "))
        data.append(no)
    print(data)

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(sum_of_squares,data) 

    pobj.close() 
    pobj.join() #Wait till all process is done

    end_time = time.perf_counter()
    
    print("Result is ")
    print(Result)

    print(f"Time required is: {end_time - start_time: .4f} seconds")


if __name__ == "__main__":
    main()

#OUTPUT
# Enter no of elements : 4
# Enter no : 1000000
# Enter no : 2000000
# Enter no : 3000000
# Enter no : 4000000
# [1000000, 2000000, 3000000, 4000000]
# Result is 
# [333333833333500000, 2666668666667000000, 9000004500000500000, 21333341333334000000]
# Time required is:  0.3123 seconds
