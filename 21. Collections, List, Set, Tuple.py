# Collection = Single "Variable" used to store multiple values
#  List  = [] ordered and changeable. Duplicates Allowed
#  Set   = {} unordered and immutable, but Add/Remove are Allowed, No Duplicates
#  Tuple = () ordered and unchangeable. Duplicates Allowed. Fastest

# List

# fruits = ["apple", "banana", "cherry", "coconut", "banana"]

# print(fruits[1])
# print(fruits[0 : 2])
# print(fruits[::2])
# print(fruits[::-1])
# for fruit in fruits:
#     print(fruit)
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)
# print("Coco" in fruits)
# fruits [0] = "pineapple"
# for fruit in fruits:
#     print(fruit)
# fruits.append("mango")
# fruits.remove("apple")
# fruits.insert(1, "grape")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.index("banana"))
# print(fruits.count("banana"))
# print(fruits.count("burger"))
# print(fruits)

# SET

# fruits = {"apple", "banana", "cherry", "coconut", "banana"}

# print(fruits)

# print(len(fruits))
# print("apple" in fruits)
# fruits.add("pineapple")
# fruits.remove("banana")
# fruits.pop()
# fruits.clear()
# print(fruits)

# Tuple

fruits = ("apple", "banana", "cherry", "coconut", "banana")

# print(dir(fruits))
# print(help(fruits))
# print("apple" in fruits)
# print(fruits.index("apple"))
# print(fruits.index("banana"))
# print(fruits.count("banana"))
# print(fruits)
for fruit in fruits:
    print(fruit)
