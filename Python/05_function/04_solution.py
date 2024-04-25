import math
radius = int(input("Enter radius of a circle"))

def circle_info(radius):
    area = math.pi * radius ** 2
    circumference = 2 * 3.14 * radius
    return area, circumference

area, circumference = circle_info(radius)

print("Area of a cricle is: ", area, "Curcumference of circle is: ", circumference)