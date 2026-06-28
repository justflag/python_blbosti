length = float(input("Enter the length of a rectangle: "))
width = float(input("Enter the width of a rectangle: "))

if length <= 0 or width <= 0:
    print("Error: Must be greater than 0")
    exit()
 
area = length * width
print(f"Area of a rectangle is: {area} cm²")