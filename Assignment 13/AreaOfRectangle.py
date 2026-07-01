# Write a program which accepts length and width of rectangle and prints area.

def calculate_area_of_rectangle(length, width):
    return length * width

def main():
   length = int(input("Enter length of the rectangle : "))
   width = int(input("Enter width of the rectangle : "))
   areaOfRectangle = calculate_area_of_rectangle(length, width)
   print("Area of rectangle is : ", areaOfRectangle)

if __name__ == "__main__":
    main()

#OUTPUT
# Enter length of the rectangle : 4
# Enter width of the rectangle : 3
# Area of rectangle is :  12
