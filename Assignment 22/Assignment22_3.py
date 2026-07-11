# For every number in the given list, count how many prime numbers exist between 1 and N using multiprocessing Pool.
# Example
# 10000
# 20000
# 30000
# 40000
# Display total prime count for each number.
import multiprocessing
import time 

def count_primes(n):
    count = 0
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count = count + 1
    return count

def main():

    data = [10000,20000,30000,40000]
    print("Input list is : ",data)
    start_time = time.perf_counter()
    pobj = multiprocessing.Pool()
    Result = pobj.map(count_primes,data)
    pobj.close()
    pobj.join()
    end_time = time.perf_counter()
    print("Total prime count for each number is : ")
    print(Result)

    print(f"Time taken is {end_time - start_time: .4f} seconds")


if __name__ == "__main__":
    main()

#OUTPUT
# Input list is :  [10000, 20000, 30000, 40000]
# Total prime count for each number is : 
# [1229, 2262, 3245, 4203]
# Time taken is  2.7385 seconds