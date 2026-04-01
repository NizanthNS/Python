
# name = input("Enter your full name: ")

# phone = input("Enter your phone number: ")

# result = len(name)
# result = name.find("N")
# result = name.rfind("n")
# result = name.rfind("q")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone.count("-")
# result = phone.replace("-", "")

# print(result)

# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ")

if len(username) > 12:
    print("Your username can't contain more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain space")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")
