# While loop = Execute some code while some conditions remains true

# name = input("Enter your name: ")
#
# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")
# print(f"Hello {name}")


# while name == "":
#     print("You did not enter your name") -- infinite loop


# age = int(input("Enter your age: "))
#
# while age < 0:
#     print("Your age cannot be negative")
#     age = int(input("Enter your age: "))
# print(f"Your age is: {age}")

# food = input("Enter your favorite food (q to Quit: ")
#
# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another favorite food (q to Quit: ")
# print("Bye")

num = int(input("Enter a number between 1 and 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Please enter a number between 1 and 10: "))
print(f"Your number is {num}")