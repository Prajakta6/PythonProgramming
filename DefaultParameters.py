#Default parameters in Python

def Area(Radius, PI = 3.14):
    Ans = PI * Radius * Radius # pi * r^2 Area of circle
    return Ans

def main():
    Ret = Area(10.5) 
    print("Area of circle is : ", Ret)

    Ret = Area(10.5, 7.15) 
    print("Area of circle is : ", Ret)

if __name__ == "__main__":
    main()