# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop

# numbers = [1, 2, 3, 4, 5, 6, 7, 8 ,9]
#
# for number in numbers:
#     print(number, end = " ")

# numbers = (1, 2, 3, 4, 5, 6, 7, 8 ,9)
#
# for number in reversed(numbers):
#     print(number)

# fruits = {"apple", "banana", "cherry"}
#
# for x in fruits:
#     print(x)

# name = "NiZ"
#
# for i in name:
#     print(i, end = "$")

dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
}

# for value in dictionary.values():
#     print(value)

for key, value in dictionary.items():
    print(f"{key} = {value}")