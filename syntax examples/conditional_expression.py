# one-line shortcut for if-else statement (ternary operator)
# print or assign one of two values based on a condition
# X if condition else Y

num = 5
a = 6
b = 7
age = 6
temp = 20
user_role = "admin"

print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Child"
weather = "HOT" if temp > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited access"

print(result)
print(max_num)
print(min_num)
print(status)
print(weather)
print(access_level)