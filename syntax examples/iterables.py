#Iterables = An object/collection that can return its elements at a time
# allowing it to be iterated over in a loop

#numbers = [1, 2, 3, 4, 5] #list
numbers = (1, 2, 3, 4, 5) #tuple

for number in reversed(numbers):
    print(number, end=" - ")

print()

fruits = {"apple", "banana", "orange", "coconut"} #set

for fruit in fruits: #cant reverse sets
    print(fruit)

print()

name = "Stepan Bargl" #string
for character in name:
    print(character, end=" ")

print()

my_dictionary = {"A": 1, "B": 2, "C": 3} #dictionary
for letter, value in my_dictionary.items():
    print(f"{letter} = {value}")
