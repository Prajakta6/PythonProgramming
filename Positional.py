#Positional parameters in Python

def Area(Radius, PI):
    Ans = PI * Radius * Radius # pi * r^2 Area of circle
    return Ans

def main():
    Ret = Area(10.5,3.14)
    print("Area of circle is : ", Ret)

    Ret = Area(13.6, 7.12)
    print("Area of circle is : ", Ret)

if __name__ == "__main__":
    main()