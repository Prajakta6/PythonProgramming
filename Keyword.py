#Keyword parameters in Python

def Area(Radius, PI):
    Ans = PI * Radius * Radius # pi * r^2 Area of circle
    return Ans

def main():
    Ret = Area(PI = 3.14, Radius = 10.5) # Here we are specifying name of variable and it's value, 
    #we have to specify all functions keywords we can't mention partial keywords to the function arguments
    print("Area of circle is : ", Ret)

    Ret = Area(PI = 3.14, 10.5) #SyntaxError: positional argument follows keyword argument

if __name__ == "__main__":
    main()