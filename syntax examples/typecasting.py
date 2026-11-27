#Typecasting = process of converting a variable from one data type to another

name = "Stepan Bargl"
age = 23
gpa = 3.2
is_student = True

print(type(name))

gpa = int(gpa) #no longer float, is int. only when printing 3
#age = float(age) #no longer int, is float
age = str(age) #no longer int, is str

age += "1"

print(gpa)
print(age)

name = bool(name) #to check wheter someone entered their name
print(name)