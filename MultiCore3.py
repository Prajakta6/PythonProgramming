import time

def SumCube(No):
    sum = 0 
    for i in range(1,No+1):
        sum = sum + (i ** 3)

    return sum

def main():
   Data = [10000000,200000000,30000000,40000000,50000000]
   Result = []

   start_time = time.perf_counter()
   for value in Data:
       Ret = SumCube(value)
       Result.append(Ret)

   end_time = time.perf_counter()

  
   print("Result is ")
   print(Result)

   print(f"Time required is: {end_time - start_time: .4f} seconds")

if __name__ == "__main__":
    main()

# OUTPUT
# Result is 
# [2500000500000025000000000000, 400000004000000010000000000000000, 202500013500000225000000000000, 640000032000000400000000000000, 1562500062500000625000000000000]
# Time required is:  21.6233 seconds