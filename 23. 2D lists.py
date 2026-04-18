
# fruits = ["apple", "banana", "cherry"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats = ["chicken", "fish", "turkey"]
#
# groceries = [fruits, vegetables, meats]
#
# fruits[0] = "pineapple"
# print(fruits)
#
# print(groceries[0])
# print(groceries[1])
# print(groceries[2])
#
# print(groceries[2][0])
#
# groceries = [["apple", "banana", "cherry"],
#              ["celery", "carrots", "potatoes"],
#              ["chicken", "fish", "turkey"]]
#
# print(groceries[2][0])
#
# for x in groceries:
#     for food in x:
#         print(food, end = " ")
#     print()

# groceries = (("apple", "banana", "cherry"),
#              ("celery", "carrots", "potatoes"),
#              ("chicken", "fish", "turkey"))
#
# print(groceries[2][0])
#
# for x in groceries:
#     for food in x:
#         print(food, end = " ")
#     print()

# groceries = ({"apple", "banana", "cherry"},
#              {"celery", "carrots", "potatoes"},
#              {"chicken", "fish", "turkey"})
#
#
# for x in groceries:
#     for food in x:
#         print(food, end = " ")
#     print()

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()