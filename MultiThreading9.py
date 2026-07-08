import time
import threading

def SumEven(No):
    print("TID od SumEven theread is : ",threading.get_ident())

def SumOdd(No):
    print("TID od SumOdd theread is : ",threading.get_ident())

def main():
   print("TID od MainThread is : ",threading.get_ident())
   start_time = time.perf_counter() #
   
   t1 = threading.Thread(target=SumEven, args=(100000000,))
   t2 = threading.Thread(target=SumOdd, args=(100000000,))
   
   t1.start()
   t2.start()
   
   t1.join()
   t2.join()

   end_time = time.perf_counter()

   print(f"Time required is : {end_time - start_time: .4f} seconds")

if __name__ == "__main__":
    main()

# OUTPUT
# TID od MainThread is :  8488017536
# TID od SumEven theread is :  6183841792
# TID od SumOdd theread is :  6200668160
# Time required is :  0.0002 seconds