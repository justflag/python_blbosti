# collection = single "variable" used to store multiple values
# list = [] orderd and changeable, Duplicates OK
# Set = {} unordered and immutable, Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicate OK. Faster

fruits = ["apple", "orange", "banana", "coconut","pineapple"]
print(dir(fruits))
print(len(fruits))
print("apple" in fruits)
print("cherry" in fruits)

fruits[0] = "cherry"
fruits[1] = "apple"
fruits.append("pear")
fruits.remove("banana")
fruits.insert(0, "pineapple")
fruits.sort()
fruits.reverse()
#fruits.clear()
print("Index is:", fruits.index("apple"))
print(fruits.count("banana"))

print(fruits[::2])
print(fruits[0:3])
print(fruits[:3])
print(fruits[::-1])

for fruit in fruits:
    print(fruit)