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

    print(f"Time required is : {end_time - start_time} seconds")

if __name__ == "__main__":
    main()

# #OUTPUT
# Enter a number : 4
# Factorial of 4 is 24
# Time required is : 1.9073486328125e-05 seconds
