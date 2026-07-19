# 2: Write a Python program to implement a class named Circle with the following requirements:
# • The class should contain three instance variables: Radius, Area, and Circumference.
# • The class should contain one class variable named PI, initialized to 3.14.
# • Define a constructor (__init__) that initializes all instance variables to O.O
# • Implement the following instance methods:
#   • Accept() - accepts the radius of the circle from the user.
#   • CalculateArea() - calculates the area of the circle and stores it in the Area variable.
#   • CalculateCircumference() - calculates the circumference of the circle and stores it in the Circumference variable.
#   • Display () - displays the values of Radius, Area, and Circumference.
# • Create multiple objects of the Circle class and invoke all the instance methods for each object.


class Circle:
    PI = 3.14 #Class variable

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    #Instance method
    def Accept(self):
        self.Radius = float(input("Enter radius of the circle: "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = Circle.PI * 2 * self.Radius

Obj1 = Circle()
Obj1.Accept()
Obj1.CalculateArea()
Obj1.CalculateCircumference()
print("Radius =", Obj1.Radius)
print("Area =", Obj1.Area)
print("Circumference =", Obj1.Circumference)

Obj2 = Circle()
Obj2.Accept()
Obj2.CalculateArea()
Obj2.CalculateCircumference()
print("Radius =", Obj2.Radius)
print("Area =", Obj2.Area)
print("Circumference =", Obj2.Circumference)

#OUTPUT 
# Enter radius of the circle: 5
# Radius = 5.0
# Area = 78.5
# Circumference = 31.400000000000002
# Enter radius of the circle: 10
# Radius = 10.0
# Area = 314.0
# Circumference = 62.800000000000004