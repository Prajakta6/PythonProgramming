#Time 
import time

def factorial(no):
    Fact = 1

    for i in range(1,no+1): 
        Fact = Fact * i 

    return Fact

def main():
    value = int(input("Enter a number : "))

    start_time = time.time()

    Ret = factorial(value)
    
    end_time = time.time()
    
    print(f"Factorial of {value} is {Ret}") #f is formatted printing

    print(f"Time required is : {end_time - start_time:.5f} seconds")

if __name__ == "__main__":
    main()

# #OUTPUT
# Enter a number : 10
# Factorial of 10 is 3628800
# Time required is : 0.00002 seconds
