# Membership = used to test whether a value or variable is found in a sequence
#              (strings, list, tuple, set or dictionary
#              1. in
#              2. not in


# word = "APPLE"
#
# letter = input("Guess a letter in the secret word: ").upper()
#
# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"There is no {letter}")

# students = {"Bob", "Alice", "Carol", "David"}
#
# student = input("Enter student name: ")
#
# if student in students:
#     print(f"Student {student} is in the list")
# else:
#     print(f"Student {student} is not in the list")

# grades = {"Bob": "A",
#           "Alice": "B",
#           "Lisa": "C",
#           "Pat": "D"}
#
# student = input("Enter a student name: ")
#
# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")

email = "nizfake@gmail.com"

if "@" in email and "." in email:
    print("The email is valid")
else:
    print("The email is not valid")
