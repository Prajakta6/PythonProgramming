# Write a program which accepts radius of circle and prints area of circle.

def calculate_area_of_circle(radius):
    return 2 * 3.14 * radius

def main():
   radius = int(input("Enter radius of the circle : "))
   areaOfCircle = calculate_area_of_circle(radius)
   print("Area of circle is : ", areaOfCircle)

if __name__ == "__main__":
    main()

#OUTPUT
# Enter radius of the circle : 10
# Area of circle is :  62.800000000000004