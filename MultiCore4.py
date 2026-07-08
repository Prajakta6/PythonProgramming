import time
import multiprocessing
import os

def SumCube(No):
    print("Process is running with PID: ",os.getpid())
    sum = 0 
    for i in range(1,No+1):
        sum = sum + (i ** 3)

    return sum

def main():
   Data = [10000000,200000000,30000000,40000000,50000000]
   Result = []

   start_time = time.perf_counter()

   pobj = multiprocessing.Pool() #Pool class object i.e. pobj. Pool class is from multiprocessing module

   Result = pobj.map(SumCube,Data) #map function is from Pool class not from FMR(Filter/Map/Reduce)

   pobj.close() 
   pobj.join() #Wait till all process is done

   end_time = time.perf_counter()

  
   print("Result is ")
   print(Result)

   print(f"Time required is: {end_time - start_time: .4f} seconds")

if __name__ == "__main__":
    main()

# OUTPUT
# Process is running with PID:  3634
# Process is running with PID:  3635
# Process is running with PID:  3631
# Process is running with PID:  3633
# Process is running with PID:  3632
# Result is 
# [2500000500000025000000000000, 400000004000000010000000000000000, 202500013500000225000000000000, 640000032000000400000000000000, 1562500062500000625000000000000]
# Time required is:  14.5838 seconds

#Note: Here all 5 PID are different so different cores are used internally by OS