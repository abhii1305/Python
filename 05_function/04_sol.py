# Create a Function that return both the Area and Circumference of a Circle given its radius
import math
def circle_stats(radius):
    area= math.pi * radius ** 2
    circumference= 2* math.pi*radius
    return area , circumference


a,c= circle_stats(3)
print("Area:",round(a,3) , "Circumference:",round(c,3))