import math
radius = float(input("Enter the radius of a circle: "))
area = math.pi * pow(radius, 2)
area2 = math.pi * (radius ** 2)
print(f"The area of the circle: {round(area, 2)}cm²")
print(f"The area of the circle: {round(area2, 2)}cm²")