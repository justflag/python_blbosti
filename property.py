#@property = Decorator used to define a method as a property (it can be accessed like an atribute)
# Benefit: add additional logic when read, write, or delete attributes
# Gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height) -> None:
        self._height = height #_ signifes protected, internal, should not be changed
        self._width = width

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")


    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

rectangel = Rectangle(3,4)
rectangel.width = 5
del rectangel.width
rectangel.height = 10
del rectangel.height

