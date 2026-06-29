# 1. user is no more than 12 characters
# 2. user must not contain spaces
# 3. user must not contain digits

username = input("Enter your username: ").lower()

if not username.isalpha():
    print("Username must not contain numbers")
elif len(username) > 12:
    print("Username must not be more than 12 characters")
elif not username.find(" ") == -1:
    print("Username must not contain spaces")
else:
    print(f"Welcome {username}")