# Conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y

#num = 5
# age = 15
# a = 1
# b = 4
# temperature = 20
user_role = "Admin"

# print("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >=18 else "Child"
# weather = "HOT" if temperature > 28 else "COLD"
access_level = "Full Access" if user_role == "Admin" else "limited access"


print(access_level)