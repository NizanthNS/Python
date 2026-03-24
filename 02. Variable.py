# Variable = A container for a value (string, integer, float, boolean)
#            A Variable behaves as if it was the value it contains

# Strings
first_name = "Niz"
last_name = "NS"
food = "Fried Chicken"
email = "nizanthns10@gmail.com"

print(f"Hello {first_name} {last_name}")
print(f"You like {food}")
print(f"Your email is {email}")

# Integers
age = 26
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class have {num_of_students} students")

# Float
price = 450.99
CGPA = 8.6
distance = 5.5

print(f"The price is {price}")
print(f"Your CGPA is {CGPA}")
print(f"You ran {distance} miles")

# Boolean

is_student = False
for_sale = True
is_online = True

if is_student:
    print(f"You are a student")
else:
    print(f"You are not a student")

if for_sale:
    print(f"The item is for sale")
else:
    print(f"The item is not for sale")

if is_online:
    print(f"You are online")
else:
    print(f"You are offline")
