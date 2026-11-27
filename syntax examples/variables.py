first_name = "Stepan"
food = "lasagne"
email = "stepan@bargl.org"

#Strings
print(first_name)
print(f"Hello,",first_name)
print(f"Hello, {first_name}")
print(f"You like {food}")
print(f"You like",food)
print(f"Your email is {email}")

#Integers
age = 23
quantity = 3
num_of_students = 29

print(f"You are {age} years old")
print(f"You are buying {3} things")
print(f"Your class has {num_of_students} students")

#Float
price = 10.99
gpa = 3.2
distance = 5.5
print(f"The price is ${price} ")
print(f"Your gpa is {gpa}")
print(f"You ran {distance} km")

#Boolean
is_student = False
for_sale = True
is_online = False

print(f"Are you a student? {is_student}")
if is_student:
    print("You are a student")
else:
    print("You are NOT a student")

if for_sale == False:
    print("That item is for sale")
else:
    print("That item is NOT available for sale")

if is_online:
    print("You are online")
else:
    print("You are offline")