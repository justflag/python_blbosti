# collection = single "variable" used to store multiple values
# list = [] orderd and changeable, Duplicates OK
# Set = {} unordered and immutable (cant change values), Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicate OK. Faster

#list
#fruits = ["apple", "orange", "banana", "coconut","pineapple"]

#print(dir(fruits))
#print(len(fruits))
#print("apple" in fruits)
#print("cherry" in fruits)

#fruits[0] = "cherry"
#fruits[1] = "apple"
#fruits.append("pear")
#fruits.remove("banana")
#fruits.insert(0, "pineapple")
#fruits.sort()
#fruits.reverse()
#fruits.clear()
#print("Index is:", fruits.index("apple"))
#print(fruits.count("banana"))

#print(fruits[::2])
#print(fruits[0:3])
#print(fruits[:3])
#print(fruits[::-1])

#for fruit in fruits:
#    print(fruit)

#set
#fruits = {"apple", "orange", "banana", "coconut","pineapple"}
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("pineapple" in fruits)

#fruits.add("cherry")
#fruits.remove("apple")
#fruits.pop()
#fruits.clear()
#print(fruits)

#tuple
#fruits = ("apple", "orange", "banana", "coconut","pineapple")
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("pineapple" in fruits)

#print(fruits.index("apple"))
#print(fruits.count("pineapple"))

#for fruit in fruits:
#    print(fruit)
