#prompts the user to enter data

name = input("What is your name?: ")
age = int(input("How old are you?: ")) #stores input as a string, need for typecasting
#age = int(age) #typecasting to int
age = age + 1
print(f"Hello {name}!")
print(f"You are {age} years old")