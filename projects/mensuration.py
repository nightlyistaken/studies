import math
print("Perimeter and area of circle")
radius = int(input("Enter the radius: "))

perimeter = 2 * math.pi * radius # use math.pi from math
area = math.pi * radius * radius 

print("Perimeter: ", perimeter)
print("Area: ", area)
