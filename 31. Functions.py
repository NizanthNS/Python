# Function = A Block of Reusable code
#            place () after the function name to invoke it

# def happy_birthday(name, age):
#     print(f"Happy Birthday to {name}")
#     print("Happy Birthday to you")
#     print("Happy Birthday to you")
#     print("Happy Birthday")
#     print("Happy Birthday")
#     print("You shouldn't be born")
#     print(f"Waste of {age} years")
#     print("You shouldn't have been born")
#     print("It would have been better if you weren't born")
#     print("Error: You shouldn't have been born")
#     print("System Message: Existence not recommended")
#     print("Fatal Error: Birth should not have occurred")
#     print()
#
# happy_birthday("Niz", 27)

# def happy_birthday(x, y):
#     print(f"Happy Birthday to {x}")
#     print("Happy Birthday to you")
#     print("Happy Birthday to you")
#     print("Happy Birthday")
#     print("Happy Birthday")
#     print("You shouldn't be born")
#     print(f"Waste of {y} years")
#     print("You shouldn't have been born")
#     print("It would have been better if you weren't born")
#     print("Error: You shouldn't have been born")
#     print("System Message: Existence not recommended")
#     print("Fatal Error: Birth should not have occurred")
#     print()
#
# happy_birthday("Niz", 27)


# def display_invoice(user_name, amount, due_date):
#     print(f"Hello {user_name}, your invoice is {amount: .2f} dollars.")
#     print(f"The due date is {due_date}")
#
# display_invoice("Niz", 100, "01-01-2026")

# return = statement used to end a function
#          and send a result back to the caller


# def add(x,y):
#     z = x + y
#     return z
#
# def subtract(x,y):
#     z = x - y
#     return z
#
# def multiply(x,y):
#     z = x * y
#     return z
#
# def divide(x,y):
#     z = x / y
#     return z
#
# print(add(4, 4))
# print(subtract(4, 4))
# print(multiply(4, 4))
# print(divide(4, 4))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("niz", "ns")

print(full_name)