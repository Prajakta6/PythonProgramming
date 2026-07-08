#Default parameters in Python

def Area(PI = 3.14, Radius): # Error: Default arguments should be always at the end - 
    #SyntaxError: parameter without a default follows parameter with a default
    Ans = PI * Radius * Radius # pi * r^2 Area of circle
    return Ans

def main():
    Ret = Area(10.5) 
    print("Area of circle is : ", Ret)

    Ret = Area(10.5, 7.15) 
    print("Area of circle is : ", Ret)

if __name__ == "__main__":
    main()