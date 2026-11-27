#Membership operators = used to test wheter a value or variable is found in a sequence
# (string, list, tuple, set, dictionary)
# 1. in
# 2. not in

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word: #returns boolean true or false
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

print()

students = {"Stepan", "Jan", "Filip"}

student = input("Enter the name of student: ")
if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")

print()

grades = {"Filip": 4, 
          "Stepan": 4, 
          "Jan": 1}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]} ")
else:
    print(f"{student} was not found.")


print()

email = "stepan@bargl.org"
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")