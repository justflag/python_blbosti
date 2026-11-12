# super() = Function used in a child class to call methods from a parent class(superclass)
# Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self,color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self): #method overwriting, using childs method not the parents
        super().describe()
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

    def describe(self): #method overwriting, using childs method not the parents
        super().describe()
        print(f"It is a square with an area of {self.width * self.width}cm^2")

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height
    def describe(self): #method overwriting, using childs method not the parents
        super().describe()
        print(f"It is a square with an area of {self.width * self.height / 2}cm^2")

circle = Circle(color = "Red", filled = True, radius=5)
square = Square(color = "Blue", filled = False, width=6)
triangle = Triangle(color = "Yellow", filled = True, width=6, height=7)
print(circle.color)
print(circle.filled)
print(f"{circle.radius} cm")
print(square.color)
print(square.filled)
print(f"{square.width} cm")
print(triangle.color)
print(triangle.filled)
print(f"{triangle.width} cm")
print(f"{triangle.height} cm")

circle.describe()
square.describe()
triangle.describe()