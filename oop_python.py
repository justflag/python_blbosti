# object = a "bundle" of related attributes (variables) and methods(functions)
# Ex. phone, cup, book
# You need a "class" to create many objects
# class = (blueprint) used to design the structure and layout of an object
from oop_import import Car
car1 = Car("Mustang", 2024, "red", False) #Instance
car2 = Car("Corvette", 2025, "blue", True) #Instance
car3 = Car("Charger", 2026, "yellow", True) #Instance

print(car1.model) # "." attribute access operator
print(car1.year)
print(car1.color)
print(car1.for_sale)
car1.drive()
car1.stop()
car1.describe()

print()
print(car2.model) # "." attribute access operator
print(car2.year)
print(car2.color)
print(car2.for_sale)
car2.drive()
print()
print(car3.model) # "." attribute access operator
print(car3.year)
print(car3.color)
print(car3.for_sale)
car3.drive()